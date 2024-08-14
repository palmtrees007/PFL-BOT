from aiogram import Bot
from aiogram.types import BotCommand


async def set_reg_aut_menu(bot: Bot):
    reg_menu_commands = [
        BotCommand(command='/cancel', description='Отменить вход/регистрацию')
    ]

    await bot.set_my_commands(reg_menu_commands)