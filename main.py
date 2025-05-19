from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

fonts = {
    "Neon": lambda text: f"✨ {text} ✨",
    "Bold": lambda text: f"**{text}**",
    "Italic": lambda text: f"*{text}*",
    "Underline": lambda text: f"__{text}__"
}

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply("سلام! متن رو بفرست تا فونت‌های نئون و مختلفش رو برات بفرستم.")

@dp.message_handler()
async def font_styles(message: types.Message):
    text = message.text
    response = ""
    for name, func in fonts.items():
        response += f"{name}:\n{func(text)}\n\n"
    await message.reply(response)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)