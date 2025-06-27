# Пользователь с фильтрами входящих апдейтов

from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery

# Фильтр, проверяющий, что входящий callback запрос - является числом
class IsDigitCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.data.isdigit()

# Фильтр, проверяющий, что входящий callback запрос - запрос на удаление закладки
class IsDelBookmarkCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.data.endswith('del') and callback.data[:-3].isdigit()