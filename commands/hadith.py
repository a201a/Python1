import telebot
import requests
from main import bot

api_url_hadith = 'https://dorar-hadith-api-one.vercel.app/v1/api/hadith/search?value='

def get_formatted_hadiths(hadiths):
    return [
        f"{hadith['hadith']}\nالراوي: {hadith['rawi']}\nالمحدث: {hadith['mohdith']}"
        f"\nالكتاب: {hadith['book']}\nالصفحة/الرقم: {hadith['numberOrPage']}"
        f"\nالتصنيف: {hadith['grade']}\n" for hadith in hadiths
    ]

@bot.message_handler(commands=['حديث'])
def search_hadith(message):
    chat_id = message.chat.id
    search_term = message.text.split(' ', 1)[1]

    try:
        response = requests.get(api_url_hadith + search_term)
        response.raise_for_status()
        hadiths = response.json()['data']
        formatted_hadiths = get_formatted_hadiths(hadiths)
        bot.send_message(chat_id, '\n'.join(formatted_hadiths))
    except requests.exceptions.RequestException as request_error:
        print('Error making request:', request_error)
        bot.send_message(chat_id, 'حدث خطأ أثناء البحث عن الأحاديث.')
    except Exception as error:
        print('Unexpected error:', error)
        bot.send_message(chat_id, 'حدث خطأ غير متوقع.')