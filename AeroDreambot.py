import telebot
from telebot import types

bot = telebot.TeleBot("")

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Цены")
item2 = types.KeyboardButton("Запись на полёт ✈")
item3 = types.KeyboardButton("Купить подарочный сертификат")
item4 = types.KeyboardButton("Основные вопросы (faq)")
item8 = types.KeyboardButton("Как нас найти")

location = types.ReplyKeyboardMarkup(resize_keyboard=True)
item5 = types.KeyboardButton("Локация")
item6 = types.KeyboardButton("Фото")
item7 = types.KeyboardButton("Назад")

inlineprice = types.InlineKeyboardMarkup(row_width=2)
item10 = types.InlineKeyboardButton("Тарифя для детей", callback_data="Тарифя для детей", url="https://aerodream.spb.ru/tariffs/tarify-dlya-detey/" )
item11 = types.InlineKeyboardButton("Тарифя для взросылх", callback_data="Тарифя для взросылх", url="https://aerodream.spb.ru/tariffs/tarify-dlya-vzroslykh/")
inlineprice.add(item10, item11)

location.add(item5, item6, item7)
menu.add(item1, item2, item3, item4, item8)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет это бот AeroDream, он может ответить на самые частые вопросы,'
                                      ' что бы открыть меню нажми на кнопку /Menu', disable_notification=True,
                     protect_content=False)


@bot.message_handler(commands=['Menu'])
def button_message(message):
    bot.send_message(message.chat.id, 'Меню', reply_markup=menu)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Запись на полёт ✈":
        bot.send_message(message.chat.id,
    " Для записи на полёт можно позвонить по номеру телефона () либо написать нашему администратору ( @79117887506)")
    elif message.text == "Основные вопросы (faq)":
        bot.send_message(message.chat.id, "Основные вопросы (faq) В РАЗРАБОТКЕ")
    elif message.text == "Как нас найти":
        bot.send_message(message.chat.id, 'Меню', reply_markup=location)
    elif message.text == "Локация":
        bot.send_location(message.chat.id, 59.87177, 30.34638)
    elif message.text == "Фото":
        bot.send_photo(message.chat.id, open('C:\\Users\\79215\\PycharmProjects\\pythonProject1\\kap.jpg', 'rb'))
    elif message.text == "Назад":
        bot.send_message(message.chat.id, 'Меню', reply_markup=menu)
    elif message.text == "Цены":
        bot.send_message(message.chat.id, "Выбирай", reply_markup=inlineprice)
    else:
        bot.send_message(message.chat.id, " я не понимаю =(")


bot.infinity_polling(timeout=1)
