import requests
import telebot
from telebot import types
from googletrans import Translator

bot = telebot.TeleBot("6849513541:AAGWIiVR0bqHoU3i9Cna9GPDpI2YNYbFq2c")

markup_promt = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn1 = types.KeyboardButton("Задать промт🖊")
markup_promt.add(btn1)


@bot.message_handler(commands=['start'])
def handler_start(message):
    name = message.chat.first_name
    bot.send_message(message.chat.id, f'<b>Привет {name}👋,\n</b>'
                                      f'<i>Я нейросеть работающая\n'
                                      f'от Яндекс сервера и я могу\n'
                                      f'ответить на любой твой\n'
                                      f'вопрос🔮.\n\n</i>'
                                      f'<b>P.S Пиши свой промт \n'
                                      f'корректно и понятно, \n'
                                      f'на английском языке.\n</b>', parse_mode='html', reply_markup=markup_promt)


@bot.message_handler(func=lambda message: message.text == 'Задать промт🖊')
def promt_message(message):
    markup = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, '<b>Напиши свой промт:</b>', parse_mode='html', reply_markup=markup)

    def promt (message):
        promt = message.text
        translator = Translator()
        result1 = translator.translate(f'{promt}', src='ru', dest='en')
        message1 = bot.send_message(message.chat.id, '<b>Генерирую ответ...⏳</b>', parse_mode='html')
        resp=requests.post(  # POST запрос
            # эндпоинт
            'http://158.160.135.104:1234/v1/chat/completions',
            # заголовок
            headers={"Content-Type": "application/json"},
            # тело запроса
            json={
                "messages": [
                    {"role": "user", "content": f'{result1.text}'},
                ],
                "temperature": 1.5,
                "max_tokens": 40
            }
        )
        data = resp.json()
        print(data)
        n = data['choices'][0]['message']['content']
        translator = Translator()
        result = translator.translate(f'{n}', src='en', dest='ru')
        bot.edit_message_text(chat_id=message.chat.id, message_id=message1.message_id, text=f'{result.text}')
        bot.send_message(message.chat.id,'Вывожу меню.', reply_markup=markup_promt)
    bot.register_next_step_handler(message, promt)




bot.polling()