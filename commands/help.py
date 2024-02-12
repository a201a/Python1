import telebot
from main import bot
@bot.message_handler(commands=['help'])
def send_help(message):
        bot.send_message(chat_id, 'حدث خطأ غير متوقع.')