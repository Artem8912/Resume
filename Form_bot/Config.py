# Модуль с информцией о конфигурации бота
import environs
from environs import Env
from dataclasses import dataclass



@dataclass    
class Tg_bot:
    bot_token:str

@dataclass
class Config:
    tg_bot:Tg_bot
    
def load_config():
    env = Env()
    env.read_env()
    return Config(tg_bot=Tg_bot(bot_token=env('BOT_TOKEN_NEW1')))
 

    