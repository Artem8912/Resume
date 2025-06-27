# Хэндлер с миддварью, фильтрующей входной апдейт от пользователя
import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from fluentogram import TranslatorHub

logger = logging.getLogger(__name__)


class TranslatorRunnerMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        user: User = data.get('event_from_user')

        if user is None:
            return await handler(event, data)

        hub: TranslatorHub = data.get('_translator_hub')
        data['i18n_en'] = hub.get_translator_by_locale(locale='en')
        data['i18n_ru'] = hub.get_translator_by_locale(locale='ru')
        data['i18n_fr'] = hub.get_translator_by_locale(locale='fr')
        return await handler(event, data)