# Модуль, содержащий функции, создающие клавиатуры объекты меню-клвиатур
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Функция для получения клавиатуры главного меню 
def get_kb() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    buttons = [InlineKeyboardButton(text = 'Создать Запрос',callback_data='create'),
           InlineKeyboardButton(text = 'Удалить Запрос',callback_data='delete_request'),
           InlineKeyboardButton(text = 'Удалить Таблицу запросов',callback_data='delete_table'),
           InlineKeyboardButton(text = 'Упорядочить запросы по указанному критерию',callback_data='order_request'),
           InlineKeyboardButton(text = 'Отобразить список запросов',callback_data='show_requests')]
    kb_builder.add(*buttons)
    kb_builder.adjust(2,2,1)

    return kb_builder.as_markup()
# Функция для получения клавиатуры меню отмены запроса
def get_cancel_kb() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.add(InlineKeyboardButton(text = 'Отменить',callback_data='cancel'))

    return kb_builder.as_markup()
# Функция для получения клавиатуры меню упорядочивания запроса по выбранному критерию
def order()->InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    buttons = [InlineKeyboardButton(text='Company',callback_data='Company'),InlineKeyboardButton(text='Technology_kind',callback_data='Technology_kind'),
               InlineKeyboardButton(text='Price',callback_data='Price'),InlineKeyboardButton(text='Weight',callback_data='Weight'),
               InlineKeyboardButton(text='Color',callback_data='Color')]
    kb_builder.add(*buttons)
    kb_builder.adjust(2,2,1)
    return kb_builder.as_markup()
# Функция для отображения базы данных всех имеющихся запросов
def get_database()->InlineKeyboardMarkup:
    kb_bulder = InlineKeyboardBuilder()
    kb_bulder.add(InlineKeyboardButton(text = 'Посмотреть базу данных',callback_data='get_base'))
    return kb_bulder.as_markup()