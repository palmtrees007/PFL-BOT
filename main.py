import asyncio

from aiogram import Bot, Dispatcher, html
from config.config import load_config
from handlers.handlers_reg import reg_router
from handlers.handlers_log import log_router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


async def main() -> None:
    
    config = load_config()

    bot = Bot(config.tg_bot.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.include_routers(reg_router, log_router)

    await dp.start_polling(bot)
    print('i love hot bebra')


if __name__ == '__main__':
    asyncio.run(main())