from copy import deepcopy
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter
from aiogram import F, Router,Bot,Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from Service.Database import (edit_monitor_info,db_start,
                              delete_table,delete_request,ordered_request)
from Keyboards.keyboards import get_kb,get_cancel_kb,get_database,order
from States.states import MonitorInfo
import random as r
import uuid

dp = Dispatcher()
user_router = Router()

@user_router.callback_query(F.data == 'cancel')
async def cmd_cancel(callback: CallbackQuery, state: FSMContext):
    if state is None:
        return

    await state.clear()
    await callback.message.answer('Вы прервали создание запроса!',reply_markup=get_kb())


@user_router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    
    await message.answer('Добрый день! Это бот для создания запросов от клиентов магазина компьютерных мониторов.',
                         reply_markup=get_kb())
    print(dp.workflow_data)
    # await create_profile(message.from_user.id)


@user_router.callback_query(F.data =='create')
async def cmd_create(callback: CallbackQuery,state:FSMContext) -> None:
    await callback.message.answer("Введите имя желаемой фирмы-производителя:",
                        reply_markup=get_cancel_kb())
    await state.set_state(state=MonitorInfo.Company)


@user_router.callback_query(F.data == 'delete_table')
async def cmd_delete_table(callback:CallbackQuery):
    await delete_table()
    await callback.message.answer('Таблица с вашими запросами полностью удалена!',reply_markup=get_kb())
    
@user_router.callback_query(F.data == 'delete_request')
async def cmd_delete_requst(callback:CallbackQuery,state:FSMContext):
    
    await callback.message.answer('Введите идентификатор запроса:')
    await state.set_state(state=MonitorInfo.Delete_request)

      
@user_router.callback_query(F.data == 'order_request')
async def sel_req(callback:CallbackQuery,state:FSMContext):
    await callback.message.answer('Выберите критерий упорядочивания',reply_markup=order())
    await state.set_state(state=MonitorInfo.Select_request)

@user_router.callback_query(F.data,StateFilter(MonitorInfo.Select_request))
async def set_criteria(callback:CallbackQuery):
    results = await ordered_request(callback.data)
    for row in results:
        await callback.message.answer(text = str(row))
    await callback.message.answer(f'Ваши запросы упорядочены по критерию <b>{callback.data}</b>!',reply_markup=get_kb())

   
@user_router.message(F.text.isdigit(),StateFilter(MonitorInfo.Delete_request))
async def del_request(message:Message):
    
    await delete_request(int(message.text))
    await message.answer('Ваш запрос успешно удалён!',reply_markup=get_kb())

@user_router.message(StateFilter(MonitorInfo.Delete_request))
async def failed_request_number(message:Message):
    await message.answer('Введите корректное значение')

@user_router.message(StateFilter(MonitorInfo.Company))
async def company(message:Message,state:FSMContext):
    await state.update_data(Company = message.text)
    await message.answer('Хорошо. Теперь введите название технологии: ',reply_markup=get_cancel_kb())
    await state.set_state(state=MonitorInfo.Technology_kind)


@user_router.message(StateFilter(MonitorInfo.Technology_kind))
async def technology(message: Message, state: FSMContext) -> None:
    await state.update_data(Technology_kind = message.text)
    await message.answer('Отлично! Введите желаемую цену ($)',reply_markup=get_cancel_kb())
    await state.set_state(state=MonitorInfo.Price)    


@user_router.message(F.text.isdigit(),StateFilter(MonitorInfo.Price))
async def price(message:Message, state: FSMContext):
    await state.update_data( Price= message.text + '$')
    await message.answer('Отлично. Теперь введите вес монитора (в кг):',reply_markup=get_cancel_kb())
    await state.set_state(state = MonitorInfo.Weight)

@user_router.message(StateFilter(MonitorInfo.Price))
async def failed_price(message:Message, state: FSMContext):
    await message.answer('Введите корректное значение')

@user_router.message(F.text.isdigit(),StateFilter(MonitorInfo.Weight))
async def weight(message: Message, state: FSMContext) -> None:
    await state.update_data( Weight = message.text + 'кг')
    
    await message.answer('Хорошо. Введите теперь желаемый цвет монитора:  ',reply_markup=get_cancel_kb())
    await state.set_state(state=MonitorInfo.Color)
    
@user_router.message(StateFilter(MonitorInfo.Weight))
async def weight(message: Message, state: FSMContext) -> None:
    await message.answer('Введите корректное значение')


@user_router.message(StateFilter(MonitorInfo.Color))
async def color(message: Message, state: FSMContext,bot:Bot) -> None:
    await state.update_data( Color = message.text)
    data = await state.get_data()
    
    Product_id = r.randint(1,1000)
    dp[f'{Product_id}'] = data
    Company = data.get('Company')
    Technology_kind = data.get('Technology_kind')
    Price = data.get('Price')
    Weight = data.get('Weight')
    Color = data.get('Color')
    await message.answer(f'<b><u>Ваш запрос:</u></b> \n <b>Id</b>: <i>{Product_id}</i> <b>Company:</b> <i>{Company}</i> <b>Technology:</b>  <i>{Technology_kind}</i>'
                         f' <b>Price:</b> <i>{Price}</i>  <b>Weight</b>  <i>{Weight}</i> <b>Color:</b> <i>{Color}</i>',parse_mode='HTML')
    await edit_monitor_info(state,Product_id)
    
    await message.answer("""'Ваш запрос успешно создан!Чтобы создать ещё один запрос -
                        'воспользуйтесь соответстующей кнопкой:'""",reply_markup=get_kb())
    # await message.answer('Посмотреть всю базу данных моих запросов',reply_markup=get_database())
    await state.clear()
    



