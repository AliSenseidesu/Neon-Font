import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router

TOKEN = os.getenv("TOKEN")
CHANNEL_USERNAME = "dlneon"  # بدون @

bot = Bot(token=TOKEN, parse_mode=ParseMode.MARKDOWN)
dp = Dispatcher(storage=MemoryStorage())
router = Router()
dp.include_router(router)

fonts = {
    "Neon": lambda text: f"✨ {text} ✨",
    "Bold": lambda text: f"**{text}**",
    "Italic": lambda text: f"*{text}*",
    "Underline": lambda text: f"__{text}__"
}

async def is_user_member(user_id: int) -> bool:
    try:
        member = await bot.get_chat_member(chat_id=f"@{CHANNEL_USERNAME}", user_id=user_id)
        return member.status in ["member", "creator", "administrator"]
    except:
        return False

@router.message(commands=["start"])
async def start(message: Message):
    if not await is_user_member(message.from_user.id):
        await message.reply(f"برای استفاده از ربات، اول عضو کانال زیر شو:\nhttps://t.me/{CHANNEL_USERNAME}")
    else:
        await message.reply("سلام! متن رو بفرست تا فونت‌های مختلفش رو دریافت کنی.")

@router.message()
async def font_styles(message: Message):
    if not await is_user_member(message.from_user.id):
        await message.reply(f"اول عضو کانال شو:\nhttps://t.me/{CHANNEL_USERNAME}")
        return

    text = message.text
    response = ""
    for name, func in fonts.items():
        response += f"{name}:\n{func(text)}\n\n"
    await message.reply(response)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
