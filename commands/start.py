import telebot

# import the bot object from main.py
from main import bot

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحبًا بك! قم بإرسال أمر معين لبدء استخدام البوت.")
