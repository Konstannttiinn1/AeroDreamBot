import telebot
from telebot import types

bot = telebot.TeleBot("5302829505:AAHUFUlvEg4q5yUwCkvaqrTRRp9WbhHPcSs")
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Запись на полёт")
item2 = types.KeyboardButton("Что одеть в полёт")
item3 = types.KeyboardButton("Где находится аэротруба")
item4 = types.KeyboardButton("Стоимость полёта")
markup.add(item1, item2, item3, item4)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет это бот AeroDream, он может ответить на самые частые вопросы,'
                                      ' что бы открыть меню нажми на кнопку /Menu', disable_notification=True,
                     protect_content=False)


@bot.message_handler(commands=['Menu'])
def button_message(message):
    bot.send_message(message.chat.id, 'Меню', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Запись на полёт":
        bot.send_message(message.chat.id,
                         " Для записи на полёт можно позвонить по номеру телефона () либо написать нашему администратору ( @79117887506)")
    elif message.text == "Что одеть в полёт":
        bot.send_message(message.chat.id, " Одевай обычную одежду ")
        elif message.text == "Что одеть в полёт":
        bot.send_message(message.chat.id, " Одевай обычную одежду ")
    elif message.text == "Где находится аэротруба":
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton("Локация")
        item6 = types.KeyboardButton("Фото")
        item7 = types.KeyboardButton("Назад")
        markup2.add(item5, item6, item7)
        bot.send_message(message.chat.id, 'Меню', reply_markup=markup2)
    elif message.text == "Локация":
        bot.send_location(message.chat.id, 59.87177, 30.34638)
    elif message.text == "Фото":
        bot.send_photo(message.chat.id, open('C:\\Users\\79215\\PycharmProjects\\pythonProject1\\kap.jpg', 'rb'))
    elif message.text == "Назад":
        bot.send_message(message.chat.id, 'Меню', reply_markup=markup)
    elif message.text == "Стоимость полёта":
        bot.send_message(message.chat.id 
    else:
        bot.send_message(message.chat.id, " я не понимаю =(")


bot.infinity_polling(timeout=1)
