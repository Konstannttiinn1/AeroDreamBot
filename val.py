import telebot
from telebot import types

certificates = types.InlineKeyboardMarkup(row_width=1)
item12 = types.InlineKeyboardButton("Ссылка на сайт", callback_data="Сертификаты", url="https://aerodream.spb.ru/certificates/" )
certificates.add(item12)

inlineprice = types.InlineKeyboardMarkup(row_width=2)
item10 = types.InlineKeyboardButton("Тарифы для детей", callback_data="Тарифя для детей", url="https://aerodream.spb.ru/tariffs/tarify-dlya-detey/" )
item11 = types.InlineKeyboardButton("Тарифы для взросылх", callback_data="Тарифя для взросылх", url="https://aerodream.spb.ru/tariffs/tarify-dlya-vzroslykh/")

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Цены")
item2 = types.KeyboardButton("Запись на полёт ✈")
item3 = types.KeyboardButton("Купить подарочный сертификат")
item4 = types.KeyboardButton("Основные вопросы (faq)")
item8 = types.KeyboardButton("Как нас найти")
menu.add(item1, item2, item3, item4, item8)

location = types.ReplyKeyboardMarkup(resize_keyboard=True)
item5 = types.KeyboardButton("Локация")
item6 = types.KeyboardButton("Фото")
item7 = types.KeyboardButton("Назад")
location.add(item5, item6, item7)

