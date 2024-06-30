import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from Config.Config import Config, load_config
from fluentogram import TranslatorHub
from handlers.other import other_router
from handlers.user import user_router
from middlewares.i18n import TranslatorRunnerMiddleware
from utils.i18n import create_translator_hub

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,format='[%(asctime)s] #%(levelname)-8s%(filename)s%(message)s'
                    '%(levelno)-8s - %(name)s - %(lineno)s')

async def main():
    logger.debug('Программа запустилась')
    conf = load_config()
    
    bot =Bot(token=conf.tg_bot.bot_token,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    
    
    translator_hub:TranslatorHub = create_translator_hub()
    
    dp.include_router(user_router)
    dp.include_router(other_router)
    
    dp.update.middleware(TranslatorRunnerMiddleware())
    
    try:
        await dp.start_polling(bot,_translator_hub=translator_hub)
    except:
        logger.debug('')
    
asyncio.run(main())
    
    
