from dataclasses import dataclass
from environs import Env
from db.db_comm import db_connect
import aiomysql


@dataclass
class DataBase:
    host: str
    user: str
    password_db: str
    database: str
    port: int


@dataclass
class TgBot:
    bot_token: str


@dataclass
class Config:
    tg_bot: TgBot
    data_base: DataBase


async def load_config(path=None):
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(bot_token=env('BOT_TOKEN')), data_base=DataBase(host=env('HOST'),
                                                                               user=env('USER'),
                                                                               password_db=env('PASSWORD_DB'),
                                                                               database=env('DATABASE'),
                                                                               port=int(env('PORT'))))