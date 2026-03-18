import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.client.session.aiohttp import AiohttpSession

# --- KONFIGURASIÝA ---
TOKEN = "8629837946:AAEJA8V2toPX5-rJLUV5gQ6X9QcZ4Esbix4"
GROUP_LINK = "https://t.me/+0NTzQ_sBQ2IwZWEy"

# PythonAnywhere Proxy sazlamasy
PROXY_URL = "http://proxy.server:3128"
session = AiohttpSession(proxy=PROXY_URL)

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN, session=session)
dp = Dispatcher()

# --- DÜWMELER ---
def language_markup():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="🇹🇲 Türkmençe", callback_data="lang_tm"))
    builder.add(types.InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"))
    return builder.as_markup()

def main_menu_tm():
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="📍 Rossiýa we Abhaziýa nokatlary"))
    builder.row(types.KeyboardButton(text="🛍 Sargyt Etmek (Çat Gruppa)"))
    builder.row(types.KeyboardButton(text="🔗 Link ugratmak"), types.KeyboardButton(text="💳 Töleg we Kartlar"))
    builder.row(types.KeyboardButton(text="💰 Bahalar & Kurs"), types.KeyboardButton(text="🌍 Dili üýtgetmek"))
    return builder.as_markup(resize_keyboard=True)

# --- FUNKSIÝALAR (HANDLERS) ---
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("🌟 Ayka Cargo-a hoş geldiňiz! Dili saýlaň:", reply_markup=language_markup())

@dp.callback_query(F.data.startswith("lang_"))
async def set_language(callback: types.CallbackQuery):
    await callback.message.answer("Esasy menýu açyldy:", reply_markup=main_menu_tm())
    await callback.answer()

@dp.message(F.text == "📍 Rossiýa we Abhaziýa nokatlary")
async def branches(message: types.Message):
    text = "🇷🇺 **Krasnodar:** +7 918 017-95-93\n🟥 **Abhaziýa:** +7 967 778-33-40"
    await message.answer(text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
