from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message
from loader import dp

router = Router()

@router.message(Command("help"))
async def bot_help(message: Message):
    text = (
        "🆘 Yordam bo‘limi:\n"
        "/start — Botni ishga tushirish\n"
        "/help — Yordam olish\n"
        "/about — Loyihadan ma’lumot"
    )
    await message.answer(text)