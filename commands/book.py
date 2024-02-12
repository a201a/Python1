import telebot
import requests
from main import bot

api_url_book = 'https://dorar-hadith-api-production.up.railway.app/v1/site/book/'

def search_book_by_name(book_name):
    url = "https://dorar-hadith-api-production.up.railway.app/v1/data/book"
    response = requests.get(url)

    if response.status_code == 200:
        books = response.json()["data"]
        matched_books = []

        for book in books:
            if book_name in book["value"]:
                matched_books.append(book)

        return matched_books
    else:
        return None

@bot.message_handler(commands=['الكتاب'])
def get_book_info_by_name(message):
    chat_id = message.chat.id
    book_name = message.text.split(' ', 1)[1]

    try:
        matched_books = search_book_by_name(book_name)
        if matched_books:
            # افتراض أنه تم العثور على كتاب واحد فقط لبساطة الشرح
            book_number = matched_books[0]["key"]
            response = requests.get(api_url_book + book_number)
            response.raise_for_status()
            book_info = response.json()['data']
            formatted_book_info = (f"اسم الكتاب: {book_info['name']}\n"
                                f"المؤلف: {book_info['author']}\n"
                                f"المحقق: {book_info['reviewer']}\n"
                                f"الناشر: {book_info['publisher']}\n"
                                f"الطبعة: {book_info['edition']}\n"
                                f"سنة الطبعة: {book_info['editionYear']}\n")
            bot.send_message(chat_id, formatted_book_info)
        else:
            bot.send_message(chat_id, "لم يتم العثور على معلومات الكتاب.")
    except requests.exceptions.RequestException as request_error:
        print('Error making request:', request_error)
        bot.send_message(chat_id, 'حدث خطأ أثناء جلب معلومات الكتاب.')
    except Exception as error:
        print('Unexpected error:', error)
        bot.send_message(chat_id, 'حدث خطأ غير متوقع.')