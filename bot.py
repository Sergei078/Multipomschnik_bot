import telebot
from buttons import markup_promt, markup, markup_menu
from SQL3 import Database, Add_promt, promt_user, requests_user, Add_requests
from googletrans import Translator
import logging
from GPT import Continue_text_gpt, Question_gpt2
from text import error, error1
from System_setting_gpt import max_tokens_in_task, count_tokens
import threading

TOKEN = input('Введи токен:')
bot = telebot.TeleBot(TOKEN)
logging.basicConfig(filename='errors.cod.log', level=logging.ERROR,
                    filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

administrators = [5586674988]
db_lock = threading.Lock()


@bot.message_handler(commands=['debug'])
def debug(message):
    user_id = message.chat.id
    if user_id in administrators:
        with open('errors.cod.log', 'rb') as er:
            bot.send_document(message.chat.id, er)
    else:
        bot.send_message(message.chat.id, 'В доступе отказано!')


@bot.message_handler(commands=['start'])
def handler_start(message):
    try:
        with db_lock:
            db_user = Database()
            try:
                if not db_user.check_user_exists(message.chat.id, message.chat.first_name):
                    db_user.add_user(message.chat.id, message.chat.first_name)
                    name = message.chat.first_name
                    bot.send_message(message.chat.id, f'<b>Привет {name}👋,\n</b>'
                                                      f'<i>Я нейросеть и я могу\n'
                                                      f'рассказать о достопри-\n'
                                                      f'мечательностях мира.\n\n</i>'
                                                      f'<b>P.S Пиши свой промт \n'
                                                      f'корректно и понятно.\n</b>',
                                     parse_mode='html', reply_markup=markup_menu)
                else:
                    name = message.chat.first_name
                    bot.send_message(message.chat.id, f'<b>Привет {name}👋,\n</b>'
                                                      f'<i>Я нейросеть и я могу\n'
                                                      f'рассказать о достопри-\n'
                                                      f'мечательностях мира.\n\n</i>'
                                                      f'<b>P.S Пиши свой промт \n'
                                                      f'корректно и понятно.\n</b>',
                                     parse_mode='html', reply_markup=markup_menu)
            finally:
                db_user.close()
    except Exception as e:
        bot.send_message(message.chat.id, '‼️Произошла непредвиденная ошибка.\n'
                                          'Попробуйте позже, если проблема остается,\n'
                                          'обратитесь за помощью!\n')
        logging.error(str(e))


@bot.message_handler(func=lambda message: message.text == 'Задать вопрос❓')
def promt_message(message):
    try:
        with db_lock:
            bot.send_message(message.chat.id, '<b>Напиши свой промт:</b>',
                             parse_mode='html', reply_markup=markup)

            def promt_user(message):
                promt = message.text
                if count_tokens(promt) > max_tokens_in_task:
                    bot.send_message(message.chat.id,"Текст задачи слишком длинный!")
                    return
                message1 = bot.send_message(message.chat.id, '<b>Генерирую ответ...⏳</b>', parse_mode='html')
                translator = Translator()
                result1 = translator.translate(f'{promt}', src='ru', dest='en')
                g = Question_gpt2()
                n1 = g.promt(result1)
                result = translator.translate(f'{n1}', src='en', dest='ru')
                user_id = message.chat.id
                add_promt = Add_promt()
                try:
                    add_promt.add_pomt(n1, user_id)
                finally:
                    add_promt.close()
                bot.edit_message_text(chat_id=message.chat.id, message_id=message1.message_id, text=f'{result.text}')
                bot.send_message(message.chat.id,'Вывожу меню.', reply_markup=markup_promt)
                requests = requests_user()
                try:
                    req = requests.promt1(user_id)
                    adding = req + 1
                finally:
                    requests.close()
                add_requests = Add_requests()
                try:
                    add_requests.add_requests(adding, user_id)
                finally:
                    add_requests.close()
            bot.register_next_step_handler(message, promt_user)
    except Exception as e:
        bot.send_message(message.chat.id, '‼️Произошла непредвиденная ошибка.\n'
                                          'Попробуйте позже, если проблема остается,\n'
                                          'обратитесь за помощью!\n')
        logging.error(str(e))


@bot.message_handler(func=lambda message: message.text == 'Продолжить✏️')
def promt_continue(message):
    try:
        with db_lock:
            user_id = message.from_user.id
            pr = promt_user()
            try:
                promt1 = pr.promt1(user_id)
            finally:
                pr.close()
            if not promt1:
                bot.send_message(message.chat.id, error1, parse_mode='html')
                return
            if len(promt1) >= 1000:
                bot.send_message(message.chat.id, error, parse_mode='html')
                return
            message2 = bot.send_message(message.chat.id, '<b>Генерирую продолжение...⏳</b>', parse_mode='html')
            n = Continue_text_gpt()
            n1 = n.gpt(promt1)
            translator = Translator()
            result = translator.translate(f'{n1}', src='en', dest='ru')
            r = promt1 + n1
            user_id = message.chat.id
            add_promt = Add_promt()
            try:
                add_promt.add_pomt(r, user_id)
            finally:
                add_promt.close()
            bot.edit_message_text(chat_id=message.chat.id, message_id=message2.message_id, text=f'{result.text}')

    except Exception as e:
        bot.send_message(message.chat.id, '‼️Произошла непредвиденная ошибка.\n'
                                          'Попробуйте позже, если проблема остается,\n'
                                          'обратитесь за помощью!\n')
        logging.error(str(e))


@bot.message_handler(func=lambda message: message.text == '👤Профиль')
def house(message):
    try:
        with db_lock:
            name = message.chat.first_name
            user_id = message.chat.id
            requests = requests_user()
            try:
                req = requests.promt1(user_id)
            finally:
                requests.close()
            bot.send_message(message.chat.id, '<b>Твой профиль👤\n\n</b>'
                                              f'<i>Имя: {name}\n'
                                              f'Кол-запросов: {req}</i>\n'
                                              f'Язык общения: Русский', parse_mode='html')
    except Exception as e:
        bot.send_message(message.chat.id, '‼️Произошла непредвиденная ошибка.\n'
                                          'Попробуйте позже, если проблема остается,\n'
                                          'обратитесь за помощью!\n')
        logging.error(str(e))


@bot.message_handler(func=lambda message: message.text == 'Вернуться в меню🏠')
def house(message):
    bot.send_message(message.chat.id, '<b>Перевожу в главное меню:</b>', parse_mode='html',
                     reply_markup=markup_menu)


@bot.message_handler(func=lambda message: message.text == 'Запустить GPT🔥')
def house(message):
    bot.send_message(message.chat.id, '<b>Перевожу в режим запросов:</b>', parse_mode='html', reply_markup=markup_promt)


bot.polling()