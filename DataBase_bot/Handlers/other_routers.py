# Импортируем необходимые классы и методы для работы с хэндлерами
from aiogram import Router
from aiogram.types import Message
# Создаём объект роутера
other_router = Router()

# Описываем хэндлер, который будет обрабатывать сообщения, не попавшие в другие хэндлеры
@other_router.message()
async def unknown_message(message:Message):
    await message.answer('Неизвестная команда')
    await message.delete()