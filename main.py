import os
import telebot

import config  # يجب وجود ملف config.py في نفس المجلد

bot = telebot.TeleBot(config.TOKEN)

# تنفيذ الأوامر الموجودة في المجلد commands
for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        exec(open(f'./commands/{filename}').read())

bot.polling()