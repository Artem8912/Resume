from aiogram.fsm.state import StatesGroup,State

class MonitorInfo(StatesGroup):
    Product_id = State()
    Company = State()
    Technology_kind = State()
    Price = State()
    Weight = State()
    Color = State()
    Delete_request = State()
    Select_request = State()