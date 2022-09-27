@bot.message_handler(commands=['start'])
def start(message):
    kb = types.InlineKeyboardMarkup()
    kb_dog = types.InlineKeyboardButton(text='Собаку', callback_data='dog')
    kb_cat = types.InlineKeyboardButton(text='Кошку', callback_data='cat')
    kb_mouse = types.InlineKeyboardButton(text='Мышь', callback_data='mouse')
    kb.add(kb_dog, kb_cat, kb_mouse)
    bot.send_message(message.chat.id, 'Привет', reply_markup=kb)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'dog':
        bot.send_message(call.message.chat.id, 'Собаку так собаку')

    elif call.data == 'cat':
        bot.send_message(call.message.chat.id, 'Котиков все любят')

    elif call.data == 'mouse':
        bot.send_message(call.message.chat.id, 'Серьёзно, мышь?')