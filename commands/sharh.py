import telebot
import requests
from main import bot

api_url_sharh = 'https://dorar-hadith-api-production.up.railway.app/v1/site/sharh/text/'

@bot.message_handler(commands=['شرح'])
def get_hadith_sharh(message):
    chat_id = message.chat.id
    hadith_id = message.text.split(' ', 1)[1]

    try:
        response = requests.get(api_url_sharh + hadith_id)
        response.raise_for_status()
        hadith_info = response.json()['data']
        formatted_hadith_sharh = (
            f"الحديث: {hadith_info['hadith']}\n"
            f"الراوي: {hadith_info['rawi']}\n"
            f"المحدث: {hadith_info['mohdith']}\n"
            f"الكتاب: {hadith_info['book']}\n"
            f"الصفحة/الرقم: {hadith_info['numberOrPage']}\n"
            f"التصنيف: {hadith_info['grade']}\n"
            f"شرح الحديث: {hadith_info['sharhMetadata']['sharh']}")
        bot.send_message(chat_id, formatted_hadith_sharh)
    except requests.exceptions.RequestException as request_error:
        print('Error making request:', request_error)
        bot.send_message(chat_id, 'حدث خطأ أثناء جلب شرح الحديث.')
    except Exception as error:
        print('Unexpected error:', error)
        bot.send_message(chat_id, 'حدث خطأ غير متوقع.')