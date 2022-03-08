from aiogram import types
#buttons
btn = types.InlineKeyboardMarkup(resize_keyboard=True,row_width=1)
lan_btn = types.InlineKeyboardMarkup(resize_keyboard=True,row_width=1)
b1 = types.KeyboardButton(text="🇺🇿O'zbek tilidan🇺🇿",callback_data='uz')
b2 = types.KeyboardButton(text="🇬🇧Ingliz tilidan🇬🇧",callback_data='en')
b3 = types.KeyboardButton(text="🇷🇺Rus tiliga🇷🇺",callback_data='ru')
b4 = types.KeyboardButton(text="🇹🇷Turk tilidan🇹🇷 ",callback_data='tr')
b5 = types.KeyboardButton(text="🇸🇦Arab tilidan🇸🇦",callback_data='ar')

b6 = types.KeyboardButton(text="🇺🇿O'zbek tiliga🇺🇿",callback_data='uz')
b7 = types.KeyboardButton(text="🇬🇧Ingliz tiliga🇬🇧",callback_data='en')
b8 = types.KeyboardButton(text="🇷🇺Rus tiliga🇷🇺",callback_data='ru')
b9 = types.KeyboardButton(text="🇹🇷Turk tiliga🇹🇷 ",callback_data='tr')
b10 = types.KeyboardButton(text="🇸🇦Arab tiliga🇸🇦",callback_data='ar')
btn.add(b1,b2,b3,b4,b5)
lan_btn.add(b6,b7,b8,b9,b10)

