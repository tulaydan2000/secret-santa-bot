import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("TOKEN")  # ← Теперь берёт из переменной Render

pairs = {
    "yue_liaaang": "teacher_25rus",
    "teacher_25rus": "Boss_Julli", 
    "Boss_Julli": "V_Kazeko",
    "V_Kazeko": "yue_liaaang"
}

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_pair(message: types.Message):
    print(f"Получил сообщение от @{message.from_user.username}")  # ОТЛАДКА
    username = message.from_user.username
    
    if username and username in pairs:
        recipient = pairs[username]
        await message.answer(f"🎁 Ты даришь подарок @{recipient}")
    else:
        await message.answer(f"❌ @{username}, ты не участвуешь в Тайном Санте")

@dp.message()
async def echo_all(message: types.Message):
    await message.answer("🤖 Бот работает! Напиши /start")

async def main():
    print("🚀 Бот запускается...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


