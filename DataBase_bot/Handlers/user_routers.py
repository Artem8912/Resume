
# Импортируем необходимые классы и методы для работы с хэндлерами
from copy import deepcopy
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter
from aiogram import F, Router,Bot,Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import default_state

# Импортируем функции, отвечающие за взаимодействие с базой данных
from Service.Database import (edit_monitor_info,db_start,
                              delete_table,delete_request,ordered_request,get_ids,show_request,add_units)
from Keyboards.keyboards import get_kb,get_cancel_kb,get_database,order
# Импортируем группу состояний, в которых может находится бот
from States.states import MonitorInfo
# Импортируем модули для генерации случайных чисел
import random as r
import uuid


# Создаём объект диспетчера и роутрера
dp = Dispatcher()
user_router = Router()

# Описываем роутер, обрабатывающий команду отмены создания запроса  
@user_router.callback_query(F.data == 'cancel')
async def cmd_cancel(callback: CallbackQuery, state: FSMContext):
    if state is None:
        return

    await state.clear()
    await callback.message.answer('Вы прервали создание запроса!',reply_markup=get_kb())

# Описываем хэндлер, обрабатывающий команду /start
@user_router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    
    await message.answer('Добрый день! Это бот для создания запросов от клиентов магазина компьютерных мониторов.',
                         reply_markup=get_kb())
    print(dp.workflow_data)
    # await create_profile(message.from_user.id)

# Описываем хэндлер, обрабатывающий команду создания запроса:
@user_router.callback_query(F.data =='create')
async def cmd_create(callback: CallbackQuery,state:FSMContext) -> None:
    await db_start()
    await callback.message.answer("Введите имя желаемой фирмы-производителя:",
                        reply_markup=get_cancel_kb())
# Помещаем бот в состояние ожидания ввода названия компании-производителя
    await state.set_state(state=MonitorInfo.Company)

# Описываем хэндлер, обрабатывающий команду удаления таблицы запросов
@user_router.callback_query(F.data == 'delete_table')
async def cmd_delete_table(callback:CallbackQuery):
    await delete_table()
    await callback.message.answer('Таблица с вашими запросами полностью удалена!',reply_markup=get_kb())
    
# Описываем хэндлер, обрабатывающий команду удаления запроса 
@user_router.callback_query(F.data == 'delete_request')
async def cmd_delete_requst(callback:CallbackQuery,state:FSMContext):
    
    await callback.message.answer('Введите идентификатор запроса:')
# Помещаем бот в состояние ожидания ввода идентификатора конкретного запроса
    await state.set_state(state=MonitorInfo.Delete_request)

# Описываем хэндлер, удаляющий запрос
@user_router.message(F.text.isdigit(),StateFilter(MonitorInfo.Delete_request))
async def del_request(message:Message,state:FSMContext):
# Получаем список запросов    
    list_ids = await get_ids()
# Если идентификатор найден в перечне    
    if int(message.text) in list_ids:
# Удаляем запрос, передавая в соответствующую функцию идентификатор        
        await delete_request(int(message.text))
        await message.answer('Ваш запрос успешно удалён!',reply_markup=get_kb())
# В противном случае:
    else:
# Выводим соответсвующее сообщение:
        await message.answer('Идентификатор не найден! Введите другой!')
# Помещаем наш бот снова в состояние ожидания ввода идентификатора:
        await state.set_state(state=MonitorInfo.Delete_request)

# Описываем хэндлер, обрабатывающий некорректно-введённые значения идентификатора
@user_router.message(StateFilter(MonitorInfo.Delete_request))
async def failed_request_number(message:Message):
    await message.answer('Введите корректное значение')

# Описываем хэндлер, упорядочивающий список запросов
@user_router.callback_query(F.data == 'order_request')
async def sel_req(callback:CallbackQuery,state:FSMContext):
    await callback.message.answer('Выберите критерий упорядочивания',reply_markup=order())
    await state.set_state(state=MonitorInfo.Select_request)
# Описываем хэндлер, обрабатывающий команду о критерии упорядочивания
@user_router.callback_query(F.data,StateFilter(MonitorInfo.Select_request))
async def set_criteria(callback:CallbackQuery,state:FSMContext):
    results = await ordered_request(callback.data)
    res = await add_units(results)
    for row in res:
        await callback.message.answer(text = str(row))
    await callback.message.answer(f'Ваши запросы упорядочены по критерию <b>{callback.data}</b>!',reply_markup=get_kb())
    await state.set_state(default_state)

   

# Описываем хэндлер, принимающий информацию о названии технологии монитора
@user_router.message(StateFilter(MonitorInfo.Company))
async def company(message:Message,state:FSMContext):
    await state.update_data(Company = message.text)
    await message.answer('Хорошо. Теперь введите название технологии: ',reply_markup=get_cancel_kb())
    await state.set_state(state=MonitorInfo.Technology_kind)

# Описываем хэндлер,  принимающий информацию о желаемом потолке цен
@user_router.message(StateFilter(MonitorInfo.Technology_kind))
async def technology(message: Message, state: FSMContext) -> None:
    await state.update_data(Technology_kind = message.text)
    await message.answer('Отлично! Введите желаемую цену ($)',reply_markup=get_cancel_kb())
    await state.set_state(state=MonitorInfo.Price)    

# Описываем хэндлер, принимающий информацию о весе монитора
@user_router.message(F.text.isdigit(),StateFilter(MonitorInfo.Price))
async def price(message:Message, state: FSMContext):
    await state.update_data( Price= int(message.text) )
    await message.answer('Отлично. Теперь введите вес монитора (в кг):',reply_markup=get_cancel_kb())
    await state.set_state(state = MonitorInfo.Weight)
# Хэндлер, реагирующий на некорректно-введённое значение веса монитора    
@user_router.message(StateFilter(MonitorInfo.Weight))
async def weight(message: Message, state: FSMContext) -> None:
    await message.answer('Введите корректное значение')
    await state.set_state(MonitorInfo.Weight)


# Описываем хэндлер, обрабатывающий некорректно-введённое значение цены
@user_router.message(StateFilter(MonitorInfo.Price))
async def failed_price(message:Message, state: FSMContext):
    await message.answer('Введите корректное значение')
    await state.set_state(MonitorInfo.Price)
    
# Описываем хэндлер, принимающий информацию о цвете монитора
@user_router.message(F.text.isdigit(),StateFilter(MonitorInfo.Weight))
async def weight(message: Message, state: FSMContext) -> None:
    await state.update_data( Weight = int(message.text))
    
    await message.answer('Хорошо. Введите теперь желаемый цвет монитора:  ',reply_markup=get_cancel_kb())
    await state.set_state(state=MonitorInfo.Color)

# Описываем хэндлер, обрабатывающий команду отображения всех запросов
@user_router.callback_query(F.data == 'show_requests')
async def show(cb:CallbackQuery):
    results = await show_request()
    
    res = await add_units(results)
    
    for row in res:
        await cb.message.answer(text = str(row))
    await cb.message.answer(text = " Список ваших запросов ",reply_markup = get_kb())


# Описываем хэндлер, выводящий информацию о созданном запросе
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
                         f' <b>Price:</b> <i>{Price}</i> $  <b>Weight</b>  <i>{Weight}</i> кг <b>Color:</b> <i>{Color}</i>',parse_mode='HTML')
    await edit_monitor_info(state,Product_id)
    
    await message.answer("""'Ваш запрос успешно создан!Чтобы создать ещё один запрос -
                        'воспользуйтесь соответстующей кнопкой:'""",reply_markup=get_kb())
   
    await state.clear()
    



