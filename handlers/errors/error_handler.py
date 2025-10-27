import logging
from aiogram import Router
from aiogram.exceptions import (
    TelegramAPIError,
    TelegramBadRequest,
    TelegramForbiddenError,
    TelegramNetworkError,
)

router = Router()
logger = logging.getLogger(__name__)

@router.errors()
async def errors_handler(event, exception):
    if isinstance(exception, TelegramBadRequest):
        logger.warning(f"⚠️ Noto‘g‘ri so‘rov: {exception}")
        return True

    elif isinstance(exception, TelegramForbiddenError):
        logger.warning(f"🚫 Botga ruxsat yo‘q (foydalanuvchi bloklagan): {exception}")
        return True

    elif isinstance(exception, TelegramNetworkError):
        logger.error(f"🌐 Tarmoq xatosi: {exception}")
        return True

    elif isinstance(exception, TelegramAPIError):
        logger.error(f"❗ Telegram API xatosi: {exception}")
        return True

    else:
        logger.exception(f"❓ Noma’lum xato: {exception}")
        return True
# So‘ng bu router’ni app.py ga ulaysiz:

#from handlers.errors import error_handler

#dp.include_router(error_handler.router)
