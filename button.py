from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# KeyboardButton bu oddiy sms xabar orqali ishlovchi buttonlar

# Tilni tanlaganda chqadigan buttonlar
uzbekcha = KeyboardButton("🇺🇿 O'zbekcha")
russion = KeyboardButton("🇷🇺 Русский")
english = KeyboardButton("🇺🇸 English")
language_btn = ReplyKeyboardMarkup( resize_keyboard=True, row_width=1, one_time_keyboard=True).add(uzbekcha, russion, english)
# end block


# O'zbekcha bo'limidagi menular uchun buttonlar
menu1 = KeyboardButton("🥘 Mashxur taomlar")
menu2 = KeyboardButton("🥗 Parxez taomlar")
menu3 = KeyboardButton("🍧 Salqin ichimliklar")
menu4 = KeyboardButton("🥬 Salatlar")
menu5 = KeyboardButton("🥠Diserlar")
menu6 = KeyboardButton("◀ Ortga")
uzbMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True).add(menu1, menu2, menu3, menu4, menu5, menu6)
# endblock



# InlineKeyboardButton Bu maxsus fungsiyalarni bajaruvchi inline button xisoblanadi va buning ko'rinishi prazrachni oyna kabi

# Maxsulotlarga buyurtma berish uchun va website ga olib otadigan buttons
purchase = InlineKeyboardMarkup(row_width=2)
order1 = InlineKeyboardButton(text="🛒 Buyutma berish 🚀 ", url="http://127.0.0.1:8000/", callback_data="buy_bow")
order2 = InlineKeyboardButton(text="📬 Izox qoldirish 🚀 ", url="http://127.0.0.1:8000/#contact", callback_data="buy_bow")
purchase.add(order1, order2)