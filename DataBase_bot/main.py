from aiogram import Dispatcher,Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import asyncio
from Config_data.config import Config,load_env
from Service.Database import db_start
from Handlers.user_routers import user_router
from Handlers.other_routers import other_router
from aiogram.fsm.storage.memory import MemoryStorage
import logging

logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(level=logging.INFO,format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
    conf = load_env()
    store = MemoryStorage()
    dp = Dispatcher(storage=store)
    bot = Bot(conf.tg_bot.bot_token,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    dp.startup.register(db_start)
    
    dp.include_router(user_router)
    dp.include_router(other_router)
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    except:
        logger.debug('')



if __name__=='__main__':
    asyncio.run(main())


