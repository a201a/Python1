import telebot
from main import bot

@bot.message_handler(func=lambda message: message.text.lower() == 'مسح')
def handle_delete_message(message):
    chat_id = message.chat.id
    delete_text = ''

    # حذف الرسالة الأخيرة
    last_message_id = message.message_id - 1
    bot.delete_message(chat_id, last_message_id)

    # أرسل رسالة جديدة تؤكد على حدوث الحذف
    bot.send_message(chat_id, delete_text)
