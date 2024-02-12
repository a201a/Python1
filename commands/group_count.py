import telebot
from main import bot

@bot.message_handler(commands=['عدد_المجموعات'])
def get_group_count(message):
    chat_id = message.chat.id
    group_count = len(bot.get_chat_administrators(chat_id))
    bot.send_message(chat_id, f"عدد المجموعات التي يتواجد فيها البوت: {group_count}")
