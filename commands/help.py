import telebot
from main import bot
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "هذا بوت تجريبي. لمزيد من المعلومات حول الأوامر المتاحة، انظر إلى الأوامر المتوفرة.")