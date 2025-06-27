# Программа для создания запросов на покупку монитора по перечню параметров
# Точка входа в проект
# Импортируем необходимые модули, классы и функции 
from aiogram import Dispatcher,Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import asyncio
from Config_data.config import Config,load_env
from Service.Database import db_start
from Handlers.user_routers import user_router
from Handlers.other_routers import other_router
from aiogram.fsm.storage.memory import MemoryStorage

# Создаём объект логгер для ведения отчёта о ходе выполнения кода программы
import logging

logger = logging.getLogger(__name__)

#Опсываем главную функцию
async def main():
    # Задаём формат вывода записей в журнале событий 
    logging.basicConfig(level=logging.INFO,format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
    # Загружаем фацл конфигурации проекта
    conf = load_env()
    
    store = MemoryStorage()
    # Создаём объект диспетчера
    dp = Dispatcher(storage=store)
    # Создаём объект нашего бота
    bot = Bot(conf.tg_bot.bot_token,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # Регистрируем функцию создания базы данных при запуске проекта
    dp.startup.register(db_start)
    # Подключаем подключаем роутеры
    dp.include_router(user_router)
    dp.include_router(other_router)
    # Пропускаем накопившиеся апдейты
    await bot.delete_webhook(drop_pending_updates=True)
    # Начинаем проверять бот на наличие обновлений
    try:
        await dp.start_polling(bot)
    except:
        logger.debug('Запуск не удался')


# Запускаем программу
if __name__=='__main__':
    asyncio.run(main())


