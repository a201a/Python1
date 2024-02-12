import telebot

# import the bot object from main.py
from main import bot

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحبًا بك في بوت الحديث الشريف!\n\n" 
"يمكنك استخدام الأوامر التالية:\n" 
"/حديث [البحث عن حديث]\n" 
"/درجة [عرض درجات الأحاديث]\n" 
"/الكتاب [معلومات عن كتاب]\n" 
"/شرح [عرض شرح لحديث]\n" 
"/المحدث [معلومات عن المحدث]")
