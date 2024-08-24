from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup

class Calc_states(StatesGroup):
    start = State()
    show_result = State()
    
    