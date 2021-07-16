import logging

# Freamwork dan keladigan va ishlashga qulay bo'lishga kerakli modullar olinadi
from aiogram import Bot, Dispatcher, executor, types

# Barcha id lar fillelar shu mobuldan keladi jumladan TOKEN ham
import config

# Barcha Button lar shu moduldan keladi va btn qisqartmasiga aylanadi
import button as btn

# Botni ishlavotganini bilib turish uchun keginchali bu o'chriladi'
print("Bot ishga tushdi.....")

# Botning aiogram freamworkda ishlayotgan polling holatini bilish uchun kerak
logging.basicConfig(level=logging.INFO)

# Kutbxonani ichidan olinga mobul barcha vazifalar kamandalar shu bilan ibrga ishlidi  misol: >> (bot.send_message("test"))
bot = Bot(token=config.TOKEN)

# Botning beriladigan kamandalarini o'z ichiga olgan o'zgaruvchi Dispatcher bu kutubxonadagi modul botni camands bolimga javob bershga kere
dp = Dispatcher(bot)

# Botga start berilganidagi kamanda va uni bajaradigan fungsiyaalri
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_photo(message.from_user.id, config.photoHello, caption=f"Привет <b>{message.from_user.first_name}</b>", parse_mode=types.ParseMode.HTML )
    await bot.send_message(message.from_user.id, "🇺🇿 O'zingizga qulay tilni tanlang,\n\n "
                                                 "🇷🇺 Выберите язык, который вам подходит \n\n "
                                                 "🇺🇸 Choose a language that suits you", reply_markup=btn.language_btn)


# Botga help berilganidagi kamanda va uni bajaradigan fungsiyaalri
@dp.message_handler(commands=['help'])
async def proces_help(message: types.Message):
    await message.reply("Yordam kerakmi?")

# O'zbekcha tanlanganida chiqadi
@dp.message_handler(lambda message: message.text == "🇺🇿 O'zbekcha")
async def menu(message: types.Message):
    await message.reply(f"Assalomalekum <b>{message.from_user.first_name}! </b> , o'zingizga kerakli taom bo'limini  tanlang",parse_mode=types.ParseMode.HTML, reply_markup=btn.uzbMenu)


# Mashxur taomlar emnusi
@dp.message_handler(lambda message: message.text == "🥘 Mashxur taomlar")
async def text(message: types.Message):
    # nomlanishi
    title = "🍗 <b>Tovuq perzulasi </b>"
    # narxi
    price = 40000

    # narx uchun convert so'm ga o'giradi
    convert = "{:,}".format(price)

    # Rasmi tagida unga izox yozadi
    caption = f"{title} \n <b> Narxi: </b> {convert} So'm"
    # user ga javob qaytaradi parse mode orqati HTML va MARKDOWN yoli bilan textlarni stile bersa bo'ladi
    await bot.send_photo(message.from_user.id, config.Куриная_перзула, caption, parse_mode=types.ParseMode.HTML, reply_markup=btn.purchase)

# Parxez taomlar emnusi
@dp.message_handler(lambda message: message.text == "🥗 Parxez taomlar")
async def text(message: types.Message):
    title = "🍗 <b> Guruch </b>"
    price = 15000
    convert = "{:,}".format(price)
    caption = f"{title} \n <b> Narxi: </b> <i> {convert} So'm </i>"
    await bot.send_photo(message.from_user.id, config.Рис, caption , parse_mode=types.ParseMode.HTML, reply_markup=btn.purchase)

# Salqin ichimliklar emnusi
@dp.message_handler(lambda message: message.text == "🍧 Salqin ichimliklar")
async def text(message: types.Message):
    title = "🍗 <b> Classic Moxito </b>"
    price1 = 25000
    price2 = 40000
    convert1 = "{:,}".format(price1)
    convert2 = "{:,}".format(price2)
    caption = f"{title} \n\n <b>💵 Narxi: </b> <i> {convert1} So'm </i> \n" \
              f"\n <b>💵 Narxi: </b> <i> {convert2} So'm </i>"
    await bot.send_photo(message.from_user.id, config.Мохито, caption , parse_mode=types.ParseMode.HTML, reply_markup=btn.purchase)

# Salatlar emnusi
@dp.message_handler(lambda message: message.text == "🥬 Salatlar")
async def text(message: types.Message):
    title = "🍗 <b> Mujskoy kapriz </b>"
    price = 35000
    convert = "{:,}".format(price)
    info = "🥚 Tuxum vareniysi, \n" \
           "🦃 Indeyka, \n" \
           "🥓 Kalbasa, \n" \
           "🥒 Bodiring, \n" \
           "🍼 Mayanez"

    caption = f"{title} \n <b>Narxi: </b> <i> {convert} So'm </i> \n" \
              f"<i> {info} </i>"
    await bot.send_photo(message.from_user.id, config.Мужской_каприз, caption , parse_mode=types.ParseMode.HTML, reply_markup=btn.purchase)

# Disert  taomlar emnusi
@dp.message_handler(lambda message: message.text == "🥠Diserlar")
async def text(message: types.Message):
    title = "🍗 <b> Shirin pirog </b>"
    price = 18000
    convert = "{:,}".format(price)
    info = ""
    caption = f"{title} \n <b>Narxi: </b> <i> {convert} So'm </i> \n" \
              f"<i> {info} </i>"
    await bot.send_photo(message.from_user.id, config.Десерт, caption , parse_mode=types.ParseMode.HTML, reply_markup=btn.purchase)



# Barchasida ortga qaytish uchun menu tilga qaytaradi
back = ["◀ Ortga", "◀ Назад", "◀ Back"]
@dp.message_handler(lambda message: message.text in back)
async def text(message: types.Message):
    await message.answer("Siz tilni tanlash  bo'limiga qaytdingiz", reply_markup=btn.language_btn)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)