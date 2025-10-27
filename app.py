import asyncio
from loader import dp, bot
from handlers.errors import error_handler
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from handlers.users import help, start, echo


async def on_startup(dispatcher):
    # Birlamchi komandalar (/start va /help)
    await set_default_commands(dispatcher)
    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


async def main():
    # Routerlarni ulaymiz
    dp.include_router(start.router)
    dp.include_router(help.router)
    dp.include_router(echo.router)

    # Startup eventini ishga tushirish
    await on_startup(bot)

    # Botni ishga tushirish
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
