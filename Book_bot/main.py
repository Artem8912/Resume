# Бот-книга
from aiogram import Dispatcher,Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import asyncio
from Config_data.config import Config,load_env
from Handlers import other_handlers, user_handlers
from Keyboards.main_menu import set_main_menu
import logging

# Создаём объект логгер для протоколирования процесса выполнения кода

logger = logging.getLogger(__name__)

# Описываем главную функцию

async def main():
# Задаём формат вывода записей в журнале событий
    logging.basicConfig(level=logging.INFO,format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
# Загружаем файл с конфигурацией бота
    config:Config = load_env()
    bot = Bot(token=config.tg_bot.bot_token,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp=Dispatcher()
# Подключаем роутеры   
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
# Загружаем главное меню
    await set_main_menu(bot)
# Пропускаем накопившиеся апдейты
    await bot.delete_webhook(drop_pending_updates=True)
# Запускаем бота
    try :
        await dp.start_polling(bot)
    except Exception as exc:
        logger.debug(f' Возникло исключение {exc}')
# Запускаем главную функцию    
asyncio.run(main())