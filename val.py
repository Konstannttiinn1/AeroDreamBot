import telebot
from telebot import types

questions = types.InlineKeyboardMarkup(row_width=2)
questions1 = types.InlineKeyboardButton("Что одеть?", callback_data="Что одеть?")
questions2 = types.InlineKeyboardButton("в какое время приходить?", callback_data="время")
questions3 = types.InlineKeyboardButton("что с собой брать?", callback_data="что с собой брать?")
questions4 = types.InlineKeyboardButton("где можно переодеться?", callback_data="где можно переодеться?")
questions5 = types.InlineKeyboardButton("Со скольки лет полёт?", callback_data="Со скольки лет полёт?")

questions.add(questions4, questions3, questions2, questions1, questions5)

certificates = types.InlineKeyboardMarkup(row_width=1)
item12 = types.InlineKeyboardButton("Ссылка на сайт", url="https://aerodream.spb.ru/certificates/" )
certificates.add(item12)

inlineprice = types.InlineKeyboardMarkup(row_width=2)
price1 = types.InlineKeyboardButton("Тарифы для детей", callback_data="Тарифы для детей", cache_time=False)
price2 = types.InlineKeyboardButton("Тарифы для взросылх", callback_data="Тарифы для взрослых")
inlineprice.add(price2, price1)

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu1 = types.KeyboardButton("Цены 💸")
menu2 = types.KeyboardButton("Запись на полёт ✈")
menu3 = types.KeyboardButton("Купить подарочный сертификат")
menu4 = types.KeyboardButton("Основные вопросы ❓")
menu8 = types.KeyboardButton("Как нас найти 🎯")
menu.add(menu1, menu2, menu3, menu4, menu8)

location = types.ReplyKeyboardMarkup(resize_keyboard=True)
location1 = types.KeyboardButton("Локация")
location2 = types.KeyboardButton("Фото")
location3 = types.KeyboardButton("Назад")
location.add(location1, location2, location3)

recordfly = "Для записи на полёт можно позвонить по номеру телефона +7(800)775-97-11  либо написать нашему администратору (@aerodream_aerotruba) \nЗаписаться на полёт или задать вопросы можно с 10 до 22"

Priceman = ("Старт - 3 минуты = 3290 руб.\nВзлёт - 5 минут = 4000 руб.\nНовичок х2 - 10 минут = 6000 руб.\nСемейный - 15 минут = 8800 руб.\nДрайв - 20 минут = 10290 руб.\nПраздник в аэротрубе - 60 минут = 24000 руб."
         "\n"
         "\nдля более подробной информацией и посмотреть акции, можно пройти по ссылке")
pricechildren = ("Старт детский - 3 минуты = 2090 руб.\nВзлёт детский - 5 минут = 3090 руб.\nНебо детский - 10 минут = 5290 руб.\nДетский праздник - 60 минут = 19990 руб."
         "\n"
         "\nдля более подробной информацией и посмотреть акции, можно пройти по ссылке")
