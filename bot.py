import telebot
from telegbot import gen_pass
kommands=("/start /pass /help /bye ")
bot=telebot.TeleBot("6033924632:AAEPrXW53y2NwjtT_4DD6jEg5p1Dyb3DHv8")
@bot.message_handler(commands=['start'])
def send_welcome(message):
        bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
        bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
        bot.reply_to(message, "Пока! Удачи!")
@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(10)  
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bot.reply_to(message, message.text)
    
bot.polling()
