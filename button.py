from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# KeyboardButton bu oddiy sms xabar orqali ishlovchi buttonlar

# Tilni tanlaganda chqadigan buttonlar
uzbekcha = KeyboardButton("๐บ๐ฟ O'zbekcha")
russion = KeyboardButton("๐ท๐บ ะ ัััะบะธะน")
english = KeyboardButton("๐บ๐ธ English")
language_btn = ReplyKeyboardMarkup( resize_keyboard=True, row_width=1, one_time_keyboard=True).add(uzbekcha, russion, english)
# end block


# O'zbekcha bo'limidagi menular uchun buttonlar
menu1 = KeyboardButton("๐ฅ Mashxur taomlar")
menu2 = KeyboardButton("๐ฅ Parxez taomlar")
menu3 = KeyboardButton("๐ง Salqin ichimliklar")
menu4 = KeyboardButton("๐ฅฌ Salatlar")
menu5 = KeyboardButton("๐ฅ Diserlar")
menu6 = KeyboardButton("โ Ortga")
uzbMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True).add(menu1, menu2, menu3, menu4, menu5, menu6)
# endblock



# InlineKeyboardButton Bu maxsus fungsiyalarni bajaruvchi inline button xisoblanadi va buning ko'rinishi prazrachni oyna kabi

# Maxsulotlarga buyurtma berish uchun va website ga olib otadigan buttons
purchase = InlineKeyboardMarkup(row_width=2)
order1 = InlineKeyboardButton(text="๐ Buyutma berish ๐ ", url="http://127.0.0.1:8000/", callback_data="buy_bow")
order2 = InlineKeyboardButton(text="๐ฌ Izox qoldirish ๐ ", url="http://127.0.0.1:8000/#contact", callback_data="buy_bow")
purchase.add(order1, order2)