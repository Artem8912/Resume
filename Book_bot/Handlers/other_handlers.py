from aiogram import Router
from aiogram.types import Message

router = Router()


# Этот хэндлер будет реагировать на любые сообщения пользователя, не попавшие в другие хэндлеры

@router.message()
async def send_echo(message: Message):
    await message.answer(f'Это эхо! {message.text}')