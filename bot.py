import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

# Render-de bu maglumatlary Environment Variables-e goşarys
API_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
ADMIN_ID = '1251341050'

API_TOKEN = os.environ.get('TELEGRAMimport logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# --- KONFIGURASIÝA ---
TOKEN = "8629837946:AAEJA8V2toPX5-rJLUV5gQ6X9QcZ4Esbix4"
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- DÜWMELER (MENÝU) ---
def language_markup():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="🇹🇲 Türkmençe", callback_data="lang_tm"))
    builder.add(types.InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"))
    return builder.as_markup()

def main_menu_tm():
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="📍 Rossiýadaky nokatlar"), types.KeyboardButton(text="🔍 Zakazy yzarlamak"))
    builder.row(types.KeyboardButton(text="🔗 Link ugratmak"), types.KeyboardButton(text="💳 Töleg we Kartlar"))
    builder.row(types.KeyboardButton(text="💰 Bahalar & Kurs"), types.KeyboardButton(text="📞 Aragatnaşyk"))
    builder.row(types.KeyboardButton(text="🌍 Dili üýtgetmek"))
    return builder.as_markup(resize_keyboard=True)

# --- FUNKSIÝALAR ---
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Ayka Cargo botuna hoş geldiňiz! Dili saýlaň / Выберите язык:", reply_markup=language_markup())

@dp.callback_query(F.data.startswith("lang_"))
async def set_language(callback: types.CallbackQuery):
    await callback.message.answer("Esasy menýu açyldy:", reply_markup=main_menu_tm())
    await callback.answer()

@dp.message(F.text == "📍 Rossiýadaky nokatlar")
async def branches(message: types.Message):
    await message.answer("📍 **Rossiýadaky nokatlarymyz:**\n• Krasnodar\n• Groznyy\n• Soçi\n• Moskwa")

@dp.message(F.text == "🔍 Zakazy yzarlamak")
async def track_order(message: types.Message):
    await message.answer("📦 ID koduňyzy ýazyň ýa-da @ayka_admin-den ýüküňiziň ýagdaýyny soraň.")

@dp.message(F.text == "🔗 Link ugratmak")
async def send_link(message: types.Message):
    await message.answer("🔗 Haýsy saýtdan haryt aljak bolsaňyz, linkini şu ýere ugradyň.")

@dp.message(F.text == "💳 Töleg we Kartlar")
async def payment_info(message: types.Message):
    await message.answer("💳 **Töleg maglumatlary:**\n\n🇹🇲 Altyn Asyr: 6011...\n🇷🇺 Sberbank: 2202...\n\nTölegden soň çegi ugradyň!")

@dp.message(F.text == "💰 Bahalar & Kurs")
async def rates_info(message: types.Message):
    await message.answer("💰 **Häzirki nyrhlar:**\n1 kg = 5$\nKursy bilmek üçin operatora ýazyň.")

@dp.message(F.text == "📞 Aragatnaşyk")
async def contact_info(message: types.Message):
    await message.answer("📞 **Habarlaşmak üçin:**\nInstagram: @ayka_cargo\nAdmin: @ayka_admin")

@dp.message(F.text == "🌍 Dili üýtgetmek")
async def change_lang(message: types.Message):
    await message.answer("Dili saýlaň / Выберите язык:", reply_markup=language_markup())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
  
