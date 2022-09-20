import telebot
from telebot import types

questions = types.InlineKeyboardMarkup(row_width=2)
questions1 = types.InlineKeyboardButton("Что одеть?", callback_data="Одевай что хочешь")
questions2 = types.InlineKeyboardButton("в какое время приходить?", callback_data="в какое время приходить?")
questions3 = types.InlineKeyboardButton("что с собой брать?", callback_data="что с собой брать?")
questions4 = types.InlineKeyboardButton("где можно переодеться", callback_data="где можно переодеться")
questions.add(questions4, questions3, questions2, questions1)

certificates = types.InlineKeyboardMarkup(row_width=1)
item12 = types.InlineKeyboardButton("Ссылка на сайт", url="https://aerodream.spb.ru/certificates/" )
certificates.add(item12)

inlineprice = types.InlineKeyboardMarkup(row_width=2)
price1 = types.InlineKeyboardButton("Тарифы для детей", url="https://aerodream.spb.ru/tariffs/tarify-dlya-detey/" )
price2 = types.InlineKeyboardButton("Тарифы для взросылх",  url="https://aerodream.spb.ru/tariffs/tarify-dlya-vzroslykh/")
inlineprice.add(price2, price1)

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu1 = types.KeyboardButton("Цены")
menu2 = types.KeyboardButton("Запись на полёт ✈")
menu3 = types.KeyboardButton("Купить подарочный сертификат")
menu4 = types.KeyboardButton("Основные вопросы")
menu8 = types.KeyboardButton("Как нас найти")
menu.add(menu1, menu2, menu3, menu4, menu8)

location = types.ReplyKeyboardMarkup(resize_keyboard=True)
location1 = types.KeyboardButton("Локация")
location2 = types.KeyboardButton("Фото")
location3 = types.KeyboardButton("Назад")
location.add(location1, location2, location3)

test = " Для записи на полёт можно позвонить по номеру телефона () либо написать нашему администратору ( @79117887506)"


