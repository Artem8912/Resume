from aiogram import Dispatcher,Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import asyncio
from Config_data.config import Config,load_env
from Handlers import other_handlers, user_handlers
from Keyboards.main_menu import set_main_menu
import logging


logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(level=logging.INFO,format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
    config:Config = load_env()
    bot = Bot(token=config.tg_bot.bot_token,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp=Dispatcher()
    
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    await set_main_menu(bot)
    
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    except:
        logger.debug('')
    
asyncio.run(main())