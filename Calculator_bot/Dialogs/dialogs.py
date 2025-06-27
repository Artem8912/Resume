
# Модуль, содержащий диалоги 
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
from aiogram.enums import ParseMode
import math

from handlers.user import router,digits1,show_result,simple_operations,squareroot,plmin,reset_screen,clear



dp=Dispatcher()


calc_dialog = Dialog(
                    Window(
                
                            Const('<b>Калькулятор</b>'),
                            Format( f'                                                  {0}'),
                            Group(
                    
                                Row(Button(text =Const( '1'),id='1',on_click=digits1),Button(text = Const('2'),id='2',on_click=digits1),Button(text = Const('3'),id='3',on_click=digits1)),
                                Row(Button(text = Const('4'),id='4',on_click=digits1),Button(text = Const('5'),id='5',on_click=digits1),Button(text = Const('6'),id='6',on_click=digits1)),
                                Row(Button(text = Const('7'),id='7',on_click=digits1),Button(text = Const('8'),id='8',on_click=digits1),Button(text = Const('9'),id='9',on_click=digits1)),
                                Row(Button(text = Const('0'),id='0',on_click=digits1),Button(text = Const('.'),id='.',on_click=digits1),Button(text = Const('+/-'),id='plusmin',on_click=plmin))
                                ),
                                Row(Button(text = Const('➕'),id='summ',on_click=simple_operations),
                                    Button(text =Const( '➖'),id='minus',on_click=simple_operations),
                                    Button(text = Const('✖️'),id='multi',on_click=simple_operations),
                                  
                                Row(Button(text=Const('➗'),id = 'divide',on_click=simple_operations),
                                    Button(text =Const( '√'),id='sqrt',on_click=squareroot),
                                    Button(text=Const('%'),id = 'procent',on_click=simple_operations),
                                    Button(text =Const( 'clear'),id='clear',on_click=clear),
                                    Button(text = Const('='),id='equal',on_click=show_result))),state = Calc_states.start,parse_mode=ParseMode.HTML
                            ),
                            Window(
                            
                                Const('<b>Калькулятор</b>'),
                                Format( '                                                   {Result}'),
                            Group(
                    
Row(Button(text =Const( '1'),id='1',on_click=digits1),Button(text = Const('2'),id='2',on_click=digits1),Button(text = Const('3'),id='3',on_click=digits1)),
Row(Button(text = Const('4'),id='4',on_click=digits1),Button(text = Const('5'),id='5',on_click=digits1),Button(text = Const('6'),id='6',on_click=digits1)),
Row(Button(text = Const('7'),id='7',on_click=digits1),Button(text = Const('8'),id='8',on_click=digits1),Button(text = Const('9'),id='9',on_click=digits1)),
Row(Button(text = Const('0'),id='0',on_click=digits1),Button(text = Const('.'),id='.',on_click=digits1),Button(text = Const('+/-'),id='plusmin',on_click=plmin))
                ),
                Row(Button(text = Const('➕'),id='summ',on_click=simple_operations),
                    Button(text =Const( '➖'),id='minus',on_click=simple_operations),
                    Button(text = Const('✖️'),id='multi',on_click=simple_operations),
                                  
                Row(Button(text=Const('➗'),id = 'divide',on_click=simple_operations),
                       Button(text =Const( '√'),id='sqrt',on_click=squareroot),
                       Button(text=Const('%'),id = 'procent',on_click=simple_operations),
                       Button(text =Const( 'clear'),id='clear',on_click=clear),
                       Button(text = Const('='),id='equal',on_click=show_result))),state = Calc_states.show_result,getter=reset_screen,parse_mode=ParseMode.HTML
                )    
                     
                     )




