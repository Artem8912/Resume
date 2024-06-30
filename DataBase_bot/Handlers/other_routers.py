from aiogram import Router
from aiogram.types import Message
other_router = Router()

@other_router.message()
async def unknown_message(message:Message):
    await message.answer('Неизвестная команда')
    await message.delete()