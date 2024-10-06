import telebot
from telebot import types
bot= telebot.TeleBot('7000130253:AAGN82T3O3C6F0WbtElJC1h0HV_gEs-dVZc')

@bot.message_handler()
def info(message):
    if message.text.lower()=='/start':
        bot.send_message(message.chat.id,f'Привет {message.from_user.first_name}, чтобы узнать информацию введи /help')
    elif message.text.lower()=='/help':
        markup=types.InlineKeyboardMarkup()
        btn1=types.InlineKeyboardButton('Листком',callback_data='Лист')
        btn2=types.InlineKeyboardButton('Камнем',callback_data='Камень')
        btn3=types.InlineKeyboardButton('Грибом',callback_data='Гриб')
        btn4=types.InlineKeyboardButton('Пельменем',callback_data='Пельмень')
        markup.row(btn1)
        markup.row(btn2)
        markup.row(btn3)
        markup.row(btn4)
        bot.send_message(message.chat.id,'С кем вы себя ассоциируете',reply_markup=markup)
    else:
        bot.send_message(message.chat.id,'Введите /help')
@bot.callback_query_handler(func=lambda callback:True)
def callback_message(callback):
    if callback.data=='Лист':
        bot.send_message(callback.message.chat.id,'Если вы ассоциируете себя как Лист, тогда вероятно вы легко'
                                                  ' приспосабливаетесь к изменениям')
    elif callback.data=='Камень':
        bot.send_message(callback.message.chat.id,'Если вы ассоциируете себя как Камень, это показывает ваш стойкий характер')
    elif callback.data=='Гриб':
        bot.send_message(callback.message.chat.id,'Если вы ассоциируете себя как Гриб, это свидетельствует о вашей '
                                                  'глубокой связи с природой')
    elif callback.data=='Пельмень':
        bot.send_message(callback.message.chat.id,'Если вы ассоциируете себя как Пельмень, значит вы добрый и веселый человек')
bot.polling(none_stop=True)