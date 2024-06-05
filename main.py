import os
import telebot
from flask import Flask
import config  # يجب وجود ملف config.py في نفس المجلد

app = Flask(__name__)
bot = telebot.TeleBot(config.TOKEN)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# تنفيذ الأوامر الموجودة في المجلد commands
for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        exec(open(f'./commands/{filename}').read())

# بدء تشغيل بوت تليجرام في خيط منفصل
import threading
telegram_thread = threading.Thread(target=bot.polling)
telegram_thread.start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))