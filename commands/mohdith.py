import telebot
import requests
from main import bot

api_url_mohdith = 'https://dorar-hadith-api-production.up.railway.app/v1/site/mohdith/'

def search_mohdith_by_name(mohdith_name):
    url = "https://dorar-hadith-api-production.up.railway.app/v1/data/mohdith"
    response = requests.get(url)

    if response.status_code == 200:
        mohdiths = response.json()["data"]
        matched_mohdiths = []

        for mohdith in mohdiths:
            if mohdith_name in mohdith["value"]:
                matched_mohdiths.append(mohdith)

        return matched_mohdiths
    else:
        return None

@bot.message_handler(commands=['المحدث'])
def get_mohdith_info(message):
    chat_id = message.chat.id
    mohdith_name = message.text.split(' ', 1)[1]

    try:
        matched_mohdiths = search_mohdith_by_name(mohdith_name)
        if matched_mohdiths:
            # افتراض أنه تم العثور على محدث واحد فقط لبساطة الشرح
            mohdith_id = matched_mohdiths[0]["key"]
            response = requests.get(api_url_mohdith + mohdith_id)
            response.raise_for_status()
            mohdith_info = response.json()['data']
            formatted_mohdith_info = (f"اسم المحدث: {mohdith_info['name']}\n"
                                    f"رقم المحدث: {mohdith_info['mohdithId']}\n"
                                    f"معلومات عن المحدث: {mohdith_info['info']}\n")
            bot.send_message(chat_id, formatted_mohdith_info)
        else:
            bot.send_message(chat_id, "لم يتم العثور على معلومات المحدث")
    except Exception as e:
        print(f"An error occurred: {e}")

