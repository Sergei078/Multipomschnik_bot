import telebot
import logging
import threading
from telebot import types
from googletrans import Translator
from buttons import markup_promt, markup, markup_menu, markup_subject, markup_level
from SQL3 import (Database, subject_user, level_user)
from GPT import Continue_text_gpt, Question_gpt2
from ERROR import error, error1, stop, error5
from System_setting_gpt import max_tokens_in_task, count_tokens
from text import Greeting
from config import BOT_TOKEN, administrators
from functions import (info_db, promt_db, promt_add, Quantity, Continue, contine_db,
                       add_contine_promt, mat, rus, chem, level1, level2, level3)


bot = telebot.TeleBot(BOT_TOKEN)

db_lock = threading.Lock()


@bot.message_handler(commands=['debug'])
def debug(message):
    user_id = message.chat.id
    if user_id in administrators:
        with open('errors.cod.log', 'rb') as file:
            bot.send_document(message.chat.id, file)
    else:
        bot.send_message(message.chat.id, stop)


@bot.message_handler(commands=['start'])
def handler_start(message):
    try:
        with db_lock:
            db_user = Database()
            try:
                if not db_user.check_user_exists(message.chat.id, message.chat.first_name):
                    db_user.add_user(message.chat.id, message.chat.first_name)
                    name = message.chat.first_name
                    start = Greeting(name)
                    bot.send_message(message.chat.id, start, parse_mode='html', reply_markup=markup_menu)
                else:
                    name = message.chat.first_name
                    start = Greeting(name)
                    bot.send_message(message.chat.id, start, parse_mode='html', reply_markup=markup_menu)
            finally:
                db_user.close()
    except Exception as e:
        bot.send_message(message.chat.id, error5)
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
                    bot.send_message(message.chat.id, "Текст задачи слишком длинный!")
                    return
                message1 = bot.send_message(message.chat.id, '<b>Генерирую ответ...⏳</b>', parse_mode='html')
                user_id = message.chat.id
                system_content = promt_db(promt, user_id)
                translator = Translator()
                result1 = translator.translate(f'{promt}', src='ru', dest='en')
                g = Question_gpt2()
                n1 = g.promt(result1, system_content)
                result = translator.translate(f'{n1}', src='en', dest='ru')
                add = promt_add(n1, user_id, result)
                bot.edit_message_text(chat_id=message.chat.id, message_id=message1.message_id, text=
                add, parse_mode='html')
                bot.send_message(message.chat.id,'Нажми Продолжить✏️\n'
                                                 'если нужны еще подробности.', reply_markup=markup_promt)
                Quantity(user_id)
            bot.register_next_step_handler(message, promt_user)
    except Exception as e:
        bot.send_message(message.chat.id, error5)
        logging.error(str(e))


@bot.message_handler(func=lambda message: message.text == 'Продолжить✏️')
def promt_continue(message):
    try:
        with db_lock:
            user_id = message.from_user.id
            promt1 = Continue(user_id)
            if not promt1:
                bot.send_message(message.chat.id, error1, parse_mode='html')
                return
            if len(promt1) >= 1000:
                bot.send_message(message.chat.id, error, parse_mode='html')
                return
            message2 = bot.send_message(message.chat.id, '<b>Генерирую продолжение...⏳</b>', parse_mode='html')
            user_id = message.chat.id
            system_content = contine_db(user_id)
            n = Continue_text_gpt()
            n1 = n.gpt(promt1,system_content)
            translator = Translator()
            result = translator.translate(f'{n1}', src='en', dest='ru')
            r = promt1 + n1
            user_id = message.chat.id
            add_contine_promt(r, user_id)
            bot.edit_message_text(chat_id=message.chat.id, message_id=message2.message_id, text=f'{result.text}')

    except Exception as e:
        bot.send_message(message.chat.id, error5)
        logging.error(str(e))


@bot.message_handler(func=lambda message: message.text == '👤Профиль')
def house(message):
    try:
        with db_lock:
            name = message.chat.first_name
            user_id = message.chat.id
            info1 = info_db(user_id, name)
            bot.send_message(message.chat.id, info1, parse_mode='html')
    except Exception as e:
        bot.send_message(message.chat.id, error5)
        logging.error(str(e))


@bot.message_handler(func=lambda message: message.text == '⚙️Настройки')
def setting(message):
    user_id = message.chat.id
    subject = subject_user()
    level = level_user()
    try:
        sub = subject.subject(user_id)
        lev = level.level(user_id)
    finally:
        level.close()
        subject.close()
    markup_setting = types.InlineKeyboardMarkup(row_width=2)
    markup_sett0 = types.InlineKeyboardButton(text='⚙️Настройки:', callback_data='0')
    markup_sett3 = types.InlineKeyboardButton(text='📚Предмет:', callback_data='0')
    markup_sett4 = types.InlineKeyboardButton(text=f'{sub}', callback_data='setting2')
    markup_sett1 = types.InlineKeyboardButton(text='👨‍🎓Уровень:', callback_data='0')
    markup_sett2 = types.InlineKeyboardButton(text=f'{lev}', callback_data='setting1')
    markup_setting.add(markup_sett0)
    markup_setting.add(markup_sett3, markup_sett4)
    markup_setting.add(markup_sett1, markup_sett2)
    bot.send_message(message.chat.id, '<b>Настройки:</b>', parse_mode='html', reply_markup=markup_setting)


@bot.callback_query_handler(func=lambda callback: callback.data == 'back')
def back(callback):
    bot.answer_callback_query(callback.id)
    user_id = callback.message.chat.id
    subject = subject_user()
    level = level_user()
    try:
        sub = subject.subject(user_id)
        lev = level.level(user_id)
    finally:
        level.close()
        subject.close()
    markup_setting = types.InlineKeyboardMarkup(row_width=2)
    markup_sett0 = types.InlineKeyboardButton(text='⚙️Настройки:', callback_data='0')
    markup_sett3 = types.InlineKeyboardButton(text='📚Предмет:', callback_data='0')
    markup_sett4 = types.InlineKeyboardButton(text=f'{sub}', callback_data='setting2')
    markup_sett1 = types.InlineKeyboardButton(text='👨‍🎓Уровень:', callback_data='0')
    markup_sett2 = types.InlineKeyboardButton(text=f'{lev}', callback_data='setting1')
    markup_setting.add(markup_sett0)
    markup_setting.add(markup_sett3, markup_sett4)
    markup_setting.add(markup_sett1, markup_sett2)
    bot.send_message(callback.message.chat.id, '<b>Настройки:</b>', parse_mode='html', reply_markup=markup_setting)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)


@bot.callback_query_handler(func=lambda callback: callback.data == 'setting2')
def subject(callback):
    bot.answer_callback_query(callback.id)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(callback.message.chat.id, '<b>Выбери предмет:</b>', parse_mode='html', reply_markup=markup_subject)


@bot.callback_query_handler(func=lambda callback: callback.data == 'subject1')
def subject_choice1(callback):
    try:
        bot.answer_callback_query(callback.id)
        user_id = callback.message.chat.id
        mat(user_id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, '<b>Вы изменили предмет!</b>', parse_mode='html')
    except Exception as e:
        bot.send_message(callback.message.chat.id, error5)
        logging.error(str(e))


@bot.callback_query_handler(func=lambda callback: callback.data == 'subject2')
def subject_choice2(callback):
    try:
        bot.answer_callback_query(callback.id)
        user_id = callback.message.chat.id
        rus(user_id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, '<b>Вы изменили предмет!</b>', parse_mode='html')
    except Exception as e:
        bot.send_message(callback.message.chat.id, error5)
        logging.error(str(e))


@bot.callback_query_handler(func=lambda callback: callback.data == 'subject3')
def subject_choice3(callback):
    try:
        bot.answer_callback_query(callback.id)
        user_id = callback.message.chat.id
        chem(user_id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, '<b>Вы изменили предмет!</b>', parse_mode='html')
    except Exception as e:
        bot.send_message(callback.message.chat.id, error5)
        logging.error(str(e))


@bot.callback_query_handler(func=lambda callback: callback.data == 'level1')
def level_choice1(callback):
    try:
        bot.answer_callback_query(callback.id)
        user_id = callback.message.chat.id
        level1(user_id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, '<b>Вы изменили уровень!</b>', parse_mode='html')
    except Exception as e:
        bot.send_message(callback.message.chat.id, error5)
        logging.error(str(e))


@bot.callback_query_handler(func=lambda callback: callback.data == 'level2')
def level_choice2(callback):
    try:
        bot.answer_callback_query(callback.id)
        user_id = callback.message.chat.id
        level2(user_id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, '<b>Вы изменили уровень!</b>', parse_mode='html')
    except Exception as e:
        bot.send_message(callback.message.chat.id, error5)
        logging.error(str(e))


@bot.callback_query_handler(func=lambda callback: callback.data == 'level3')
def level_choice3(callback):
    try:
        bot.answer_callback_query(callback.id)
        user_id = callback.message.chat.id
        level3(user_id)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, '<b>Вы изменили уровень!</b>', parse_mode='html')
    except Exception as e:
        bot.send_message(callback.message.chat.id, error5)
        logging.error(str(e))


@bot.callback_query_handler(func=lambda callback: callback.data == 'setting1')
def level(callback):
    bot.answer_callback_query(callback.id)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(callback.message.chat.id, '<b>Выбери уровень:</b>', parse_mode='html', reply_markup=markup_level)


@bot.message_handler(func=lambda message: message.text == 'Вернуться в меню🏠')
def house(message):
    bot.send_message(message.chat.id, '<b>Перевожу в главное меню:</b>', parse_mode='html',
                     reply_markup=markup_menu)


@bot.message_handler(func=lambda message: message.text == 'Запустить GPT🔥')
def house(message):
    bot.send_message(message.chat.id, '<b>Перевожу в режим запросов:</b>', parse_mode='html', reply_markup=markup_promt)


bot.polling()