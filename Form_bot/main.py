from aiogram.types import Message,CallbackQuery,InlineKeyboardButton,InlineKeyboardMarkup
from aiogram import Bot,Dispatcher,F
from aiogram.client.default import DefaultBotProperties
import logging,random
import asyncio
from Config import load_config
from aiogram.filters import CommandStart,Command,BaseFilter
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.user import User
from aiogram.fsm.state import State,StatesGroup,default_state
from aiogram.filters import StateFilter,invert_f,or_f,and_f
from aiogram.fsm.context import FSMContext
from aiogram_dialog import Dialog,DialogManager,Window,widgets
from aiogram_dialog.widgets.text import Const,Format
from aiogram_dialog.widgets.utils import Group,List


conf = load_config()

dp = Dispatcher()
bot = Bot(token=conf.tg_bot.bot_token,default=DefaultBotProperties(parse_mode='HTML'))

 
class StatesForm(StatesGroup):
    Name = State()
    Surname = State()
    Age = State()
    Gender = State()
    Description = State()
    Photo = State()
    
class finished_form_filter(BaseFilter):
    def __init__(self,dat:dict[str,str]):
        self.dat = dat
    async def __call__(self,message:Message)->bool:
        
        return len(self.dat) ==len(dp.workflow_data.get('buttons'))+1   
        

def get_kb()->InlineKeyboardMarkup:
            
    kb_build = InlineKeyboardBuilder()
    label = '✅'
    bt_1 = InlineKeyboardButton(text='Age',callback_data='age')
    bt_2 = InlineKeyboardButton(text='Gender',callback_data='gender')
    bt_3 = InlineKeyboardButton(text='Name',callback_data='name')
    bt_4 = InlineKeyboardButton(text='Surname',callback_data='surname')
    bt_5 = InlineKeyboardButton(text='Description',callback_data='desk')
    bt_6 = InlineKeyboardButton(text='Photo',callback_data='photo')
    buttons = [bt_1,bt_2,bt_3,bt_4,bt_5,bt_6]
    dp.workflow_data.update({'buttons':buttons})
    for button in buttons:
        if button.callback_data in dp.workflow_data.values():
            button.text +=" "+ label
    kb_build.add(*buttons)
    kb_build.adjust(1,2,2)
    return kb_build.as_markup()

@dp.message(CommandStart())
async def com_start(message:Message,state:FSMContext):
    await message.answer(text='Приступим к заполнению анкеты. Выберите опцию:',reply_markup=get_kb())
    
    await state.set_state(state=default_state)



@dp.callback_query(F.data == 'name')
async def command_name(callback:CallbackQuery,state:FSMContext):
    await callback.message.answer(text='Введите ваше имя')
    dp.workflow_data.update({'name':'name'}) 
    await state.set_state(StatesForm.Name)
    

@dp.message(F.text.isalpha(),lambda x :len(x.text)<20,StateFilter(StatesForm.Name))
async def enter_name(message:Message,state:FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(default_state)
    await message.answer(text= 'Отлично, ваше имя сохранено! Для продолжения нажмите \'/follow\'')
    

@dp.message(Command(commands='follow'),finished_form_filter(dp.workflow_data))
async def finished_form(message:Message):
    await message.answer(text = 'Ваша анкета готова!'+' Чтобы посмотреть - нажмите /watch_form',reply_markup=get_kb())   
@dp.message(Command(commands='follow'),StateFilter(default_state))
async def cmd_default(message:Message):
            
    await message.answer(text='Выберите следующую опцию:',reply_markup=get_kb())

@dp.message(StateFilter(StatesForm.Name))
async def failed_name(message:Message,state:FSMContext):
    await message.answer(text = 'Введите корректное имя')
    await state.set_state(StatesForm.Name)
    
@dp.message(Command(commands='watch_form'))
async def watch_form(message:Message,state:FSMContext):
    form = await state.get_data()
    surname =  form.get('surname')
    name =  form.get('name')
    age =  form.get('age')
    gender = form.get('gender')
    desc = form.get('desk')
    await message.answer(f'<b>Имя</b>: - <i>{name}</i>\n'
                            f'<b>Фамилия</b>: - <i>{surname}</i>\n'
                            f'<b>Возраст</b>:- <i>{age}</i>\n'
                            f'<b>Пол</b>: - <i> {gender}</i>\n'
                            f'<b>О себе</b>: - <i>{desc}</i>\n')
    await message.answer_photo(photo=form.get('photo'),caption='<u>Фото</u>')
    await state.clear()
    dp.workflow_data.clear()
    await message.answer(text = 'Для составления новой анкеты - нажмите /start')

@dp.callback_query(F.data == 'surname')
async def command_surname(callback:CallbackQuery,state:FSMContext):
    await callback.message.answer(text='Введите свою фамилию')
    dp.workflow_data.update({'surname':'surname'})
    await state.set_state(StatesForm.Surname)
    
@dp.message(F.text.isalpha(),lambda x :len(x.text)<15,StateFilter(StatesForm.Surname))
async def enter_surname(message:Message,state:FSMContext):
    await state.update_data(surname = message.text)
    
    
    await message.answer(text= 'Отлично, ваша фамилия сохранена! Для продолжения нажмите \'/follow\'')
    await state.set_state(default_state)

@dp.message(StateFilter(StatesForm.Surname))
async def failed_surname(message:Message,state:FSMContext):
    await message.answer(text = 'Введите корректную фамилию')
    await state.set_state(StatesForm.Surname)    
    
@dp.callback_query(F.data == 'age')
async def command_age(callback:CallbackQuery,state:FSMContext):
    await callback.message.answer(text='Введите ваш возраст')
    dp.workflow_data.update({'age':'age'})
    await state.set_state(StatesForm.Age)
    
@dp.message(F.text.isdigit(),lambda x: 2<int(x.text)<150,StateFilter(StatesForm.Age))
async def enter_age(message:Message,state:FSMContext):
    await state.update_data(age = message.text)
    await message.answer(text= 'Отлично, ваш возраст сохранён! Для продолжения нажмите \'/follow\'')
    await state.set_state(default_state)   
    
@dp.message(StateFilter(StatesForm.Age))
async def failed_age(message:Message,state:FSMContext):
    await message.answer(text = 'Введите корректный возраст')
    await state.set_state(StatesForm.Age) 
    
@dp.callback_query(F.data == 'gender')
async def command_gender(callback:CallbackQuery,state:FSMContext):
    
    dp.workflow_data.update({'gender':'gender'})
    bt1 = InlineKeyboardButton(text='M',callback_data='Men')
    bt2 = InlineKeyboardButton(text='Ж',callback_data='Woman')
    buttons_gender = [bt1,bt2]
    kb_buld = InlineKeyboardBuilder()
    kb_buld.add(*buttons_gender)
    kb_buld.adjust(2)
    await callback.message.answer(text = 'Выберите ваш пол',reply_markup=kb_buld.as_markup())
    await state.set_state(StatesForm.Gender)
    
@dp.callback_query(F.data,StateFilter(StatesForm.Gender))
async def enter_gender(callback:CallbackQuery,state:FSMContext):
    await state.update_data(gender = callback.data)
    await callback.message.answer(text= 'Отлично, ваш пол сохранён! Для продолжения нажмите \'/follow\'')
    await state.set_state(default_state)

@dp.callback_query(F.data == 'desk')
async def command_description(callback:CallbackQuery,state:FSMContext):
    await callback.message.answer(text='Введите ваше описание')
    dp.workflow_data.update({'desk':'desk'})
    await state.set_state(StatesForm.Description)
    
@dp.message(StateFilter(StatesForm.Description))
async def enter_description(message:Message,state:FSMContext):
    await state.update_data(desk = message.text)
    await message.answer(text= 'Отлично, ваше описание сохранёно! Для продолжения нажмите \'/follow\'')
    await state.set_state(default_state)       
@dp.callback_query(F.data == 'photo')
async def command_photo(callback:CallbackQuery,state:FSMContext):
    await callback.message.answer(text='Загрузите вашу фотографию')
    
    dp.workflow_data.update({'photo':'photo'})
    await state.set_state(StatesForm.Photo)
    
@dp.message(StateFilter(StatesForm.Photo),F.photo)
async def load_photo(message:Message,state:FSMContext):
    await state.update_data(photo = message.photo[0].file_id)
    await message.answer(text= 'Отлично, ваша фотография загружена! Для продолжения нажмите \'/follow\'')
    
    await state.set_state(default_state)
    
@dp.message()
async def unkown_command(message:Message):
    await message.answer('Неизвестная команда')


if __name__=='__main__':
    dp.startup.register()
    dp.run_polling(bot)