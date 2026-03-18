import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.client.session.aiohttp import AiohttpSession

# --- KONFIGURASIÝA ---
TOKEN = "8629837946:AAEJA8V2toPX5-rJLUV5gQ6X9QcZ4Esbix4"
GROUP_LINK = "https://t.me/+0NTzQ_sBQ2IwZWEy"

# PythonAnywhere Mugt akkount üçin hökman gerek
PROXY_URL = "http://proxy.server:3128"
session = AiohttpSession(proxy=PROXY_URL)

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN, session=session)
dp = Dispatcher()

# --- DÜWMELER (KEYBOARDS) ---

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

def main_menu_ru():
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="📍 Филиалы в России и Абхазии"))
    builder.row(types.KeyboardButton(text="🛍 Сделать заказ (Чат группа)"))
    builder.row(types.KeyboardButton(text="🔗 Отправить ссылку"), types.KeyboardButton(text="💳 Оплата и карты"))
    builder.row(types.KeyboardButton(text="💰 Цены и Курс"), types.KeyboardButton(text="🌍 Сменить язык"))
    return builder.as_markup(resize_keyboard=True)

# --- FUNKSIÝALAR (HANDLERS) ---

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("🌟 Ayka Cargo botuna hoş geldiňiz! Dili saýlaň / Добро пожаловать! Выберите язык:", 
                         reply_markup=language_markup())

@dp.callback_query(F.data.startswith("lang_"))
async def set_language(callback: types.CallbackQuery):
    if callback.data == "lang_tm":
        await callback.message.answer("Esasy menýu açyldy:", reply_markup=main_menu_tm())
    else:
        await callback.message.answer("Главное меню открыто:", reply_markup=main_menu_ru())
    await callback.answer()

@dp.message(F.text.in_(["📍 Rossiýa we Abhaziýa nokatlary", "📍 Филиалы в России и Абхазии"]))
async def branches(message: types.Message):
    text = (
        "🇷🇺 **Rossiýadaky nokatlar / Филиалы в России:**\n"
        "• Krasnodar: +7 918 017-95-93\n"
        "• Karaçaýewsk: +7 909 499-51-07\n"
        "• Tümen: +7 909 307-21-90\n"
        "• Groznyý: +7 918 705-93-97\n"
        "• Esentüki: +7 919 758-46-50\n"
        "• Stawrapol: +7 963 285-49-79\n\n"
        "🟥✋⭐ **Abhaziýadaky nokatlar / Филиалы в Абхазии:**\n"
        "• Сухум: +7 967 778-33-40, +7 940 725-70-82\n"
        "• Гагра: +7 968 461-40-30"
    )
    await message.answer(text)

@dp.message(F.text.in_(["🌍 Dili üýtgetmek", "🌍 Сменить язык"]))
async def change_lang(message: types.Message):
    await message.answer("Dili saýlaň / Выберите язык:", reply_markup=language_markup())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
