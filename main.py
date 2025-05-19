import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router

TOKEN = os.getenv("TOKEN")

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

@router.message(commands=["start"])
async def start(message: Message):
    await message.reply("سلام! متن رو بفرست تا فونت‌های نئون و مختلفش رو برات بفرستم.")

@router.message()
async def font_styles(message: Message):
    text = message.text
    response = ""
    for name, func in fonts.items():
        response += f"{name}:\n{func(text)}\n\n"
    await message.reply(response)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
