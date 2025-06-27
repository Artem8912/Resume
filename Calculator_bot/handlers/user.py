# Модуль, содержащий хэндлеры, обрабатывающие наатие на разные кнопки калькулятора
from aiogram.types import Message,CallbackQuery,InlineKeyboardButton,InlineKeyboardMarkup
from aiogram import Bot,Dispatcher,F
from aiogram.client.default import DefaultBotProperties
import logging,random
import asyncio
from aiogram import Router
from aiogram.filters import CommandStart,Command,BaseFilter
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.user import User
from aiogram.fsm.state import State,StatesGroup,default_state
from aiogram.filters import StateFilter,invert_f,or_f,and_f
from aiogram.fsm.context import FSMContext
from aiogram_dialog import Dialog,DialogManager,Window,widgets,StartMode
from aiogram_dialog.widgets.text import Const,Format
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.utils import Group,List
from States.states import Calc_states

import math
# Создаём объект диспетчера
dp = Dispatcher()
# Создаём объект роутера
router = Router()
  

# Хэндлер, обрабатывающий команду /start
@router.message(CommandStart())
async def start(message:Message,dialog_manager:DialogManager,state:FSMContext):
    dp['number2'] = ''
    await dialog_manager.start(state=Calc_states.start,mode =StartMode.RESET_STACK)


# Функция, очищающая экран
async def reset_screen(dialog_manager:DialogManager,**kwargs):
    return {'Result':dp['result'] }

# Функция, выполняющая команды ввода цифр
async def digits1(callback:CallbackQuery,state:FSMContext,dialog_manager:DialogManager):
    
        dp['number2']+=callback.data
        await callback.answer(text = callback.data)
 
# Функция, выполняющая простейшие операции (сложение, деление, вычитание, умножение)
async def simple_operations(callback:CallbackQuery,state:FSMContext,dialog_manager:DialogManager):
    dp['number1'] = dp['number2']
    dp['number2'] = ''
    dp.workflow_data.update({'operation':callback.data})
    
# Функция, выполняющая команду извлечения квадратного корня
async def squareroot(callback:CallbackQuery,state:FSMContext,dialog_manager:DialogManager):
    dp.workflow_data.update({'operation':callback.data})
    await callback.answer(text = callback.data)

# Функция, добаляющая знак минус к числу 
async def plmin(callback:CallbackQuery,dialog_manager:DialogManager,button:Button):
    dp['number2']+='-'
    await callback.answer(text = callback.data)
# Функция, очищающая экран    
async def clear(callback:CallbackQuery,button:Button,dialog_manager:DialogManager):
    await dialog_manager.switch_to(state=Calc_states.start)
    await callback.answer(text = 'CLEARED')
# Функция, показывающая результат     
async def show_result(callback:CallbackQuery,button:Button,dialog_manager:DialogManager ):
    if dp.workflow_data.get('operation') == 'summ':
        result = float(dp['number1']) + float(dp['number2'])
    elif dp.workflow_data.get('operation') == 'multi':
        result = float(dp['number1']) * float(dp['number2'])
    elif dp.workflow_data.get('operation') == 'minus':
        result = float(dp['number1']) - float(dp['number2'])
    elif dp.workflow_data.get('operation') == 'divide':
        result = float(dp['number1']) / float(dp['number2'])
    elif dp.workflow_data.get('operation') == 'sqrt':
        try :
            result = math.sqrt(float(dp['number2']))
        except :
            await callback.message.answer('Введите, пожалуйста, неотрицательное число!')
            dp['number2'] = ''
            return
    elif dp.workflow_data.get('operation') == 'procent':
        if '-' not in  dp['number1'] and '-' not in  dp['number2']:
            result = (float(dp['number1'])/100) * (float(dp['number2']))
            
            
        else:
            await callback.message.answer('Введите, пожалуйста, неотрицательные числа!')
            dp['number1'] = ''
            dp['number2'] = ''
            return
    dp.workflow_data.update({'result':result})
    # await callback.message.answer(text = f'Результат: {dp['result']}')
    await dialog_manager.start(state=Calc_states.show_result,data={'Result':dp['result'] })

    dp['number1'] = ''
    dp['number2'] = ''
    return result
    