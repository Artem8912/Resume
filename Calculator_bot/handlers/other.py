from aiogram import Router
from aiogram import F,Bot
from aiogram.types import Message,CallbackQuery


additional_router = Router()

# @additional_router.message(F.text != '/start')
# async def greeting(message:Message):
#     await message.answer('Добрый день! Чтобы начать работу с калькулятором нажмите /start')
    
@additional_router.message()
async def unkown_command(message:Message):
    
    await message.answer(text = 'Пожалуйста, воспользуйтесь кнопками!')
    await message.delete()
    
    



