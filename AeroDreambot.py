from telebot import types
from val import *

bot = telebot.TeleBot("")
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Меню', reply_markup=menu)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    print(message)
    if message.text == "Запись на полёт ✈":
        bot.send_message(message.chat.id, recordfly)
    elif message.text == "Основные вопросы ❓":
        bot.send_message(message.chat.id, "Основные вопросы", reply_markup=questions)
    elif message.text == "Как нас найти 🎯":
        bot.send_message(message.chat.id, 'Меню', reply_markup=location)
    elif message.text == "Локация":
        bot.send_location(message.chat.id, 59.87177, 30.34638)
    elif message.text == "Фото":
        bot.send_photo(message.chat.id, open('C:\\Users\\79215\\PycharmProjects\\pythonProject1\\kap.jpg', 'rb'))
    elif message.text == "Назад":
        bot.send_message(message.chat.id, 'Меню', reply_markup=menu)
    elif message.text == "Цены 💸":
        bot.send_message(message.chat.id, "Тарифы", reply_markup=inlineprice)
    elif message.text == "Купить подарок 🎁":
        bot.send_message(message.chat.id, "купить подарочный сертификат", reply_markup=certificates)
    elif message.text == "Контакты 📞":
        bot.send_message(message.chat.id, contacts)
    else:
        bot.send_message(message.chat.id, "я не понимаю =(")

@bot.callback_query_handler(func=lambda call: True)
def cal(call):
    print(call)
    if call.data == "дети":
        bot.send_message(call.message.chat.id, "Дети летают с 5 лет" "\nДетьми считются до 14 лет включительно"
                                                "\nДети летают с инструкторами")
    elif call.data == "полёт":
        bot.send_message(call.message.chat.id, "Летаем всегда друг за другом, по очереди и с инструктором")
    elif call.data == "вес":
        bot.send_message(call.message.chat.id, "Летаем до 120 кг")
    elif call.data == "билеты":
        ticket = types.InlineKeyboardMarkup(row_width=2)
        sert = types.InlineKeyboardButton("Сертификат", callback_data="сертификат")
        ticket2 = types.InlineKeyboardButton("Билет", callback_data="билет")
        ticket.add(sert, ticket2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=ts, reply_markup=ticket)
    elif call.data == "билет":
        bot.send_photo(call.message.chat.id, open("C:\\Users\\79215\\Downloads\\photo_2022-10-16_18-34-39.jpg", "rb"))
    elif call.data == "сертификат":
        bot.send_photo(call.message.chat.id, open("C:\\Users\\79215\\Downloads\\photo_2022-10-16_18-34-27.jpg", "rb"))
    elif call.data == "срок":
        bot.send_message(call.message.chat.id, "Срок действия электронного билета и подарочного сертификата 9 месяцев")
    elif call.data == "бронь":
        bot.send_message(call.message.chat.id, "Работаем по предварительной записи со среды по воскресенье полёты проходят С 11 до 19"
                         "\nЗаписаться можно по номеру телефона +7(800)775-97-11 или написать нашему администратору @aerodream_aerotruba")
    elif call.data == "Тарифы для детей":
        bot.send_message(call.message.chat.id, pricechildren)
    elif call.data == "Тарифы":
        bot.send_message(call.message.chat.id, Priceman)



bot.infinity_polling(timeout=0.5)
