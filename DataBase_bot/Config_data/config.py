# Модуль, содержащий информацию о файле конфигурации
from dataclasses import dataclass
from environs import Env

@dataclass
class Tg_bot:
    bot_token:str
    

@dataclass
class Config:
    tg_bot:Tg_bot
    
def load_env():
    env=Env()
    env.read_env()
    return Config(
        Tg_bot(bot_token=env('BOT_TOKEN1')))