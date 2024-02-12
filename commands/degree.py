import telebot
import requests
from main import bot

api_url_degree = 'https://dorar-hadith-api-production.up.railway.app/v1/data/degree'

@bot.message_handler(commands=['درجة'])
def get_hadith_degrees(message):
    chat_id = message.chat.id

    try:
        response = requests.get(api_url_degree)
        response.raise_for_status()
        degrees = response.json()['data']
        formatted_degrees = '\n'.join(
            [f"{degree['key']}: {degree['value']}" for degree in degrees])
        bot.send_message(chat_id, formatted_degrees)
    except requests.exceptions.RequestException as request_error:
        print('Error making request:', request_error)
        bot.send_message(chat_id, 'حدث خطأ أثناء جلب درجات الأحاديث.')
    except Exception as error:
        print('Unexpected error:', error)
        bot.send_message(chat_id, 'حدث خطأ غير متوقع.')