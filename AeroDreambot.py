import telebot
from telebot import types
import val

bot = telebot.TeleBot("5046580563:AAF7g_LQHTOoxV4rmnAJG6Dbb4yTmK6ETRM")
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
    if call.data == "дети":
        bot.send_message(call.message.chat.id, "Дети летают с 5 лет" "\nДетьми считются до 14 лет включительно"
                                                "\nДети летают с инструкторами")
    elif call.data == "полёт":
        bot.send_message(call.message.chat.id, "Летаем всегда друг за другом, по очереди и с инструктором")
    elif call.data == "вес":
        bot.send_message(call.message.chat.id, "Летаем до 120 кг")
    elif call.data == "билеты":
        bot.send_message(call.message.chat.id,"Отличие между ними только в оформлении. Электронный билет приходит на почту"
                         "\nПодарочный сертификат- это симпатичная коробочка, формата А6, внутри инструкция и сам сертификат в виде открытки")
    elif call.data == "срок":
        bot.send_message(call.message.chat.id, "Срок действия электронного билета и подарочного сертификата 9 месяцев")
    elif call.data == "бронь":
        bot.send_message(call.message.chat.id, "Работаем по предварительной записи со среды по воскресенье полёты проходят С 11 до 19"
                         "\nЗаписаться можно по номеру телефона +7(800)775-97-11 или написать нашему администратору @aerodream_aerotruba")
    elif call.data == "Тарифы для детей":
        bot.send_message(call.message.chat.id, val.pricechildren)
    elif call.data == "Тарифы":
        bot.send_message(call.message.chat.id, val.Priceman)



bot.infinity_polling(timeout=0.5)