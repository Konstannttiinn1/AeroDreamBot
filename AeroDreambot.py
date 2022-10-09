import telebot
from telebot import types
import val

bot = telebot.TeleBot("5302829505:AAHUFUlvEg4q5yUwCkvaqrTRRp9WbhHPcSs")
x = 1
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Меню', reply_markup=val.menu)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Запись на полёт ✈":
        bot.send_message(message.chat.id, val.recordfly)
    elif message.text == "Основные вопросы ❓":
        bot.send_message(message.chat.id, "Основные вопросы", reply_markup=val.questions)
    elif message.text == "Как нас найти 🎯":
        bot.send_message(message.chat.id, 'Меню', reply_markup=val.location)
    elif message.text == "Локация":
        bot.send_location(message.chat.id, 59.87177, 30.34638)
    elif message.text == "Фото":
        bot.send_photo(message.chat.id, open('C:\\Users\\79215\\PycharmProjects\\pythonProject1\\kap.jpg', 'rb'))
    elif message.text == "Назад":
        bot.send_message(message.chat.id, 'Меню', reply_markup=val.menu)
    elif message.text == "Цены 💸":
        bot.send_message(message.chat.id, "Тарифы", reply_markup=val.inlineprice)
    elif message.text == "Купить подарочный сертификат":
        bot.send_message(message.chat.id, "купить подарочный сертификат", reply_markup=val.certificates)
    else:
        bot.send_message(message.chat.id, " я не понимаю =(")

@bot.callback_query_handler(func=lambda call: True)
def cal(call):
    if call.data == "Что одеть?":
        bot.send_message(call.message.chat.id, "Тест одежда")
    elif call.data == "время":
        bot.send_message(call.message.chat.id, "во время")
    elif call.data == "что с собой брать?":
        bot.send_message(call.message.chat.id, "настроение")
    elif call.data == "где можно переодеться?":
        bot.send_message(call.message.chat.id, "переодется можно у нас")
    elif call.data == "Тарифы для детей":
        bot.send_message(call.message.chat.id, val.pricechildren)
    elif call.data == "Тарифы для взрослых":
        bot.send_message(call.message.chat.id, val.Priceman)


bot.infinity_polling(timeout=0.5)