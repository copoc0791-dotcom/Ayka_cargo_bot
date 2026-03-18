import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

# Render-de bu maglumatlary Environment Variables-e goşarys
API_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
ADMIN_ID = '1251341050'

API_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
API_TOKEN = "8629837946:AAEJA8V2toPX5-rJLUV5gQ6X9QcZ4Esbix4"

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    kb = InlineKeyboardMarkup(row_width=2).add(
        InlineKeyboardButton("Türkmençe 🇹🇲", callback_data="l_tm"),
        InlineKeyboardButton("Русский 🇷🇺", callback_data="l_ru")
    )
    await message.answer("🌟 Ayka Cargo-a hoş geldiňiz!\nDil saýlaň / Выберите язык:", reply_markup=kb)

@dp.callback_query_handler(lambda c: c.data in ['l_tm', 'l_ru'])
async def set_lang(c: types.CallbackQuery):
    await c.answer() # Bu düwmäniň işlemegi üçin iň möhüm setir!
    lang = "tm" if c.data == "l_tm" else "ru"
    
    phone_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
        KeyboardButton("📱 Belgi ugratmak / Отправить номер", request_contact=True)
    )
    
    msg = "📞 Telefon belgiňizi ugradyň:" if lang == "tm" else "📞 Отправьте ваш номер телефона:"
    await bot.send_message(c.from_user.id, msg, reply_markup=phone_kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
  
