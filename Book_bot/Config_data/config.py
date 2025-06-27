# Модуль с информацией о конфигурации бота
from dataclasses import dataclass
from environs import Env

@dataclass
class Tg_bot:
    bot_token:str
    admin_ids: list[int]

@dataclass
class Config:
    tg_bot:Tg_bot
    
def load_env():
    env=Env()
    env.read_env()
    return Config(
        Tg_bot(bot_token=env('BOT_TOKEN'),admin_ids=env('ADMIN_IDS')))