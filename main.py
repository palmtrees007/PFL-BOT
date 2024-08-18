import asyncio

from aiogram import Bot, Dispatcher, html
from config.config import load_config
from handlers.handlers_reg import reg_router
from handlers.handlers_log import log_router
from handlers.handlers_base import main_router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from db.db_comm import db_connect


async def main() -> None:
    
    config = await load_config()

    bot = Bot(config.tg_bot.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.include_routers(reg_router, log_router, main_router)

    pool = await db_connect(host=config.data_base.host,
               port=config.data_base.port,
               user=config.data_base.user,
               password=config.data_base.password_db,
               database=config.data_base.database)
    max_lobby = 0

    dp.workflow_data.update({'pool': pool})

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())