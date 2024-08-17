from dataclasses import dataclass
from environs import Env
from db.db_comm import db_connect


@dataclass
class TgBot:
    bot_token: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path=None):
    env = Env()
    env.read_env(path)
    connection = db_connect(host=env('HOST'),
               port=env('PORT'),
               user=env('USER'),
               password=env('PASSWORD_DB'),
               database=env('DATABASE'))
    return Config(tg_bot=TgBot(bot_token=env('BOT_TOKEN'))), connection