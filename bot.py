import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# --- KONFIGURASIÝA ---
TOKEN = "8629837946:AAEJA8V2toPX5-rJLUV5gQ6X9QcZ4Esbix4"
GROUP_LINK = "https://t.me/+0NTzQ_sBQ2IwZWEy"
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
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

# --- FUNKSIÝALAR ---

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("🌟 Ayka Cargo-a hoş geldiňiz! / Добро пожаловать!", reply_markup=language_markup())

@dp.callback_query(F.data.startswith("lang_"))
async def set_language(callback: types.CallbackQuery):
    await callback.message.answer("Esasy menýu açyldy:", reply_markup=main_menu_tm())
    await callback.answer()

@dp.message(F.text == "📍 Rossiýa we Abhaziýa nokatlary")
async def branches(message: types.Message):
    text = (
        "🇷🇺 **Rossiýadaky nokatlar:**\n"
        "• Krasnodar: +7 918 017-95-93 (Jemal)\n"
        "• Karaçaýewsk: +7 909 499-51-07 (Daniýa)\n"
        "• Tümen: +7 909 307-21-90 (Bäşim)\n"
        "• Wladikawkaz: +7 918 705-93-97 (Akgurban)\n"
        "• Groznyý: +7 918 705-93-97 (Akgurban)\n"
        "• Esentüki: +7 919 758-46-50 (Güneş)\n"
        "• Stawrapol: +7 963 285-49-79 (Babageldi)\n"
        "• Rostow, Soçi, Adler: (Operatora ýazyň)\n\n"
        "🇬🇪 **Abhaziýadaky nokatlar:**\n"
        "• Сухум: +7 967 778-33-40 (Ынам), +7 940 725-70-82 (Аннуш)\n"
        "• Гагра: +7 968 461-40-30 (Мерген)"
    )
    await message.answer(text)

@dp.message(F.text == "🛍 Sargyt Etmek (Çat Gruppa)")
async def join_group(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="➡️ Çat Gruppa Geç", url=GROUP_LINK))
    await message.answer("Sargyt etmek üçin biziň ýörite çat gruppamyza goşulyň:", reply_markup=builder.as_markup())

@dp.message(F.photo | F.text.contains("http"))
async def handle_pricing(message: types.Message):
    await message.reply(
        "✅ Sargyt maglumaty kabul edildi!\n\n"
        "💰 **Siziň tölemeli bahasynyňyz:** 150 TMT\n"
        "Töleg etmek üçin aşakdaky '💳 Töleg we Kartlar' düwmesine basyň."
    )

@dp.message(F.text == "💳 Töleg we Kartlar")
async def payment_step(message: types.Message):
    await message.answer(
        "💳 **Töleg maglumatlary:**\n\n"
        "🇹🇲 Altyn Asyr: (Kart belgiňiz)\n"
        "🇷🇺 Sberbank: (Kart belgiňiz)\n\n"
        "Tölegden soň çegiň suratyny şu ýere ugradyň!"
    )

@dp.message(F.photo & F.caption.contains("töleg") | F.document)
async def confirm_payment(message: types.Message):
    await message.answer("✅ **Tölegiňiz kabul edildi!**\nSargydyňyz tassyklanyldy.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
