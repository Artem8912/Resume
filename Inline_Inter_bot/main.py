# Программа для отображения информации о сайтах тур-агентств на различных языках

# Импортируем необходимые классы и модули
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


# Создаём объект логгер для протоколирования процесса выполнения кода
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,format='[%(asctime)s] #%(levelname)-8s%(filename)s%(message)s'
                    '%(levelno)-8s - %(name)s - %(lineno)s')
# Описываем главную функцию
async def main():
    
    logger.debug('Программа запустилась')
    # Загружаем файл конфигурации
    conf = load_config()
    # Создаём объект бота
    bot =Bot(token=conf.tg_bot.bot_token,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    
    # Создаём объект translator_hub, содержащий информацию о локалях с переводами
    translator_hub:TranslatorHub = create_translator_hub()
    # Подключаем роутеры с прикреплёнными к ним хэндлерами
    dp.include_router(user_router)
    dp.include_router(other_router)
    # Подключаем мидлварь
    dp.update.middleware(TranslatorRunnerMiddleware())
    # Запускаем бота
    try:
        await dp.start_polling(bot,_translator_hub=translator_hub)
    except Exception as exc:
        logger.debug(f'Возникло исключение {exc} ')
    
asyncio.run(main())
    
    
