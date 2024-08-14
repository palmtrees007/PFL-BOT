from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    bot_token: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path=None):
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(bot_token=env('BOT_TOKEN')))