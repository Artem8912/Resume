from aiogram.types import Message,CallbackQuery,InlineKeyboardButton,InlineKeyboardMarkup
from aiogram import Bot,Dispatcher,F
from aiogram.client.default import DefaultBotProperties
import logging,random
import asyncio
from aiogram.filters import CommandStart,Command,BaseFilter
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.user import User
from aiogram.fsm.state import State,StatesGroup,default_state
from aiogram.filters import StateFilter,invert_f,or_f,and_f
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode
from aiogram_dialog import Dialog,DialogManager,Window,widgets,setup_dialogs
from aiogram_dialog.widgets.text import Const,Format
from aiogram_dialog.widgets.utils import Group,List
from Config.config import Config,load_config
from Dialogs.dialogs import calc_dialog
from aiogram.fsm.storage.redis import Redis,RedisStorage
redis = Redis(host='localhost')

storage = RedisStorage(redis=redis)


from handlers.user import router
from handlers.other import additional_router



logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(level=logging.INFO,format='%(filename)s:%(lineno)d #%(levelname)-8s '
                '[%(asctime)s] - %(name)s - %(message)s')
    logger.info(msg='Программа запустилась')

    conf = load_config()
    
    dp= Dispatcher()
    bot = Bot(token =conf.tg_bot.bot_token,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    dp.include_router(router)
    dp.include_router(additional_router)
    
    dp.include_router(calc_dialog)
    
    setup_dialogs(dp)
    
    
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except:
        logger.debug(msg='Возникла ошибка')


if __name__=='__main__':
    asyncio.run(main())
   
