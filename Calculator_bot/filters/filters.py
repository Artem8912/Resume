from aiogram.types import Message,CallbackQuery,InlineKeyboardButton,InlineKeyboardMarkup
from aiogram import Bot,Dispatcher,F
from aiogram.client.default import DefaultBotProperties
import logging,random
from aiogram.filters import CommandStart,Command,BaseFilter
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.user import User
from aiogram.fsm.state import State,StatesGroup,default_state
from aiogram.filters import StateFilter,invert_f,or_f,and_f
from aiogram.fsm.context import FSMContext
from aiogram_dialog import Dialog,DialogManager,Window,widgets,StartMode
from aiogram_dialog.widgets.text import Const,Format
from aiogram_dialog.widgets.kbd import Column,Row,Button,Group,ListGroup
from aiogram_dialog.widgets.utils import List
from States.states import Calc_states
from handlers.user import Result,num1,num2

class ButtonDigit_id_filter(BaseFilter):
    def __init__(self,b_id):
        self.b_id = b_id
    def __call__(message:Message,dialog_manager:DialogManager)->bool:
         return dialog_manager.dialog_data