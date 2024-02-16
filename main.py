import telebot
from telebot import types

bot = telebot.TeleBot("6890847203:AAG-2lBvgnH5nWIUKc99VN5noAjQC16KFFo")


@bot.message_handler(commands=['start'])
def handle_start(message):
    with open('Masha_i_Medved_-_S_Dnem_Rozhdeniya_MENYA_74147456.mp3', 'rb') as f1:
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup_start = types.InlineKeyboardButton(text='Погнали🔥', callback_data='start')
        markup.add(markup_start)
        bot.send_message(message.chat.id, '<b>Здравствуй Мария👋\n\n</b>'
                                          '<i>Меня зовут Ботик😎\n'
                                          'Я поздравлю тебя\n'
                                          'С днем рождения🎉,желаю\n'
                                          'чтобы все было хорошо,\n'
                                          'все твои цели и мечты\n'
                                          'сбились, и самое главное\n'
                                          'никогда не грусти. В\n'
                                          'этом боте ты вспомнишь\n'
                                          'прошлое время, как ты его\n'
                                          'проводила,и свое настоящее\n'
                                          'время, и все самые крутые и\n'
                                          'интересные моменты\n\n</i>'
                                          '<b>Приятного просмотра☺️</b>', parse_mode='html', reply_markup=markup)
        bot.send_audio(message.chat.id, f1)


@bot.callback_query_handler(func=lambda callback: callback.data == 'sc')
def calback(callback):
    bot.answer_callback_query(callback.id)
    markup0 = types.InlineKeyboardMarkup(row_width=2)
    markup01 = types.InlineKeyboardButton(text='Любимые треки🎧', callback_data='music')
    markup0.add(markup01)
    bot.send_message(callback.message.chat.id, '<b>Создатели проекта:\n\n</b>'
                                               '<i>Сергей - разработчик\n'
                                               'Анастасия - монтажер\n'
                                               'Ксения - монтажер</i>\n\n'
                                               '<b>Ну получается что все,\n'
                                               'нажми на кнопку чтобы\n'
                                               'перейти к любым трекам</b>', parse_mode='html', reply_markup=markup0)


@bot.callback_query_handler(func=lambda callback: callback.data == 'music')
def music(callback):
    bot.answer_callback_query(callback.id)
    with open('Sergejj_Lazarev_-_V_samoe_serdce_53298542.mp3', 'rb') as f1:
        with open('By_Indiya_The_Limba_-_money_76487041.mp3', 'rb') as f2:
            with open('bjembi_aikko_-_Tak_neinteresno_75542910.mp3', 'rb') as f3:
                bot.send_audio(callback.message.chat.id, f1)
                bot.send_audio(callback.message.chat.id, f2)
                bot.send_audio(callback.message.chat.id, f3)
                bot.send_message(callback.message.chat.id, 'Хорошего проведения ДР🎉')


@bot.callback_query_handler(func=lambda callback: callback.data)
def scenes_callback_id(callback):
    bot.answer_callback_query(callback.id)
    if callback.data == 'start':
        with open('video_2024-02-02_19-35-20.mp4', 'rb') as f:
            with open('video_2024-02-02_19-38-08.mp4', 'rb') as f1:
                with open('video_2024-02-02_19-43-53.mp4', 'rb') as f2:
                    message = bot.send_message(callback.message.chat.id, 'Видео загружаются...')
                    bot.send_video(callback.message.chat.id, f, timeout=50)
                    bot.send_video(callback.message.chat.id, f1, timeout=50)
                    bot.send_video(callback.message.chat.id, f2, timeout=50)
                    bot.delete_message(callback.message.chat.id, message.message_id)
                    markup = types.InlineKeyboardMarkup(row_width=2)
                    markup_start = types.InlineKeyboardButton(text='Дальше➡️', callback_data='scooll')
                    markup.add(markup_start)
                    bot.send_message(callback.message.chat.id, '<b>Посмотри эти видео\n'
                                                               'и вспомни те самые \n'
                                                               'моменты в которых было \n'
                                                               'весело😃, грустно😢, \n'
                                                               'но самое главное ты \n'
                                                               'проходила это все со \n'
                                                               'своими друзьями.</b>\n',
                                     parse_mode='html', reply_markup=markup)
    if callback.data == 'scooll':
        with open('video_2024-02-02_20-11-15.mp4', 'rb') as a:
            message = bot.send_message(callback.message.chat.id, 'Видео загружается...')
            bot.send_video(callback.message.chat.id, a, timeout=50)
            bot.delete_message(callback.message.chat.id, message.message_id)
            markup1 = types.InlineKeyboardMarkup(row_width=2)
            markup_start1 = types.InlineKeyboardButton(text='Дальше➡️', callback_data='scooll1')
            markup1.add(markup_start1)
            bot.send_message(callback.message.chat.id, '<b>Те самые школьные \n'
                                                       'времена когда уроки \n'
                                                       'были по 45 минут, \n'
                                                       'любимая школьная \n'
                                                       'столовая, любимые друзья, \n'
                                                       'все это пролетело очень \n'
                                                       'быстро но все те моменты \n'
                                                       'мы никогда не забудем!</b>',
                             parse_mode='html', reply_markup=markup1)
    if callback.data == 'scooll1':
        with open('video_2024-02-02_20-30-31.mp4', 'rb') as b7:
            message = bot.send_message(callback.message.chat.id, 'Видео загружается...')
            bot.send_video(callback.message.chat.id, b7, timeout=50)
            bot.delete_message(callback.message.chat.id, message.message_id)
            markup2 = types.InlineKeyboardMarkup(row_width=2)
            markup_start2 = types.InlineKeyboardButton(text='И что-же это все??😢', callback_data='sco')
            markup2.add(markup_start2)
            bot.send_message(callback.message.chat.id, '<b>Вот уже и наступил тот\n'
                                                        'самый момент когда уже\n'
                                                        'закончила школу и \n'
                                                        'поступила в колледж.\n'
                                                        'Так сказать начало\n'
                                                        'взрослой жизни.</b>',
                             parse_mode='html', reply_markup=markup2)
    if callback.data == 'sco':
        markup3 = types.InlineKeyboardMarkup(row_width=2)
        markup_start3 = types.InlineKeyboardButton(text='Ну что-же там???😱', callback_data='scene1')
        markup3.add(markup_start3)
        bot.send_message(callback.message.chat.id, '<b>Конечно же нет!!\n'
                                                       'Мы пока только на середине.\n'
                                                       'Ты даже не представляешь,\n'
                                                       'что тебя ждет сейчас😊\n</b>',
                         parse_mode='html', reply_markup=markup3)
    if callback.data == 'scene1':
        with open('video45.mp4', 'rb') as b:
            message = bot.send_message(callback.message.chat.id, 'Видео загружается...')
            bot.send_video(callback.message.chat.id, b, timeout=50)
            bot.send_message(callback.message.chat.id, '<i>Поздравление от Полины</i>',
                             parse_mode='html')
            bot.delete_message(callback.message.chat.id, message.message_id)
            markup4 = types.InlineKeyboardMarkup(row_width=2)
            markup_start4 = types.InlineKeyboardButton(text='Следующее поздравление🎉', callback_data='scene2')
            markup4.add(markup_start4)
            bot.send_message(callback.message.chat.id, 'Теперь смотрим\n'
                                                       'поздравления людей😊\n',
                             parse_mode='html', reply_markup=markup4)
    if callback.data == 'scene2':
        with open('IMG_8137.MOV', 'rb') as b:
            message = bot.send_message(callback.message.chat.id, 'Видео загружается...')
            bot.send_video(callback.message.chat.id, b, timeout=50)
            markup5 = types.InlineKeyboardMarkup(row_width=2)
            markup_start5 = types.InlineKeyboardButton(text='Следующее поздравление🎉', callback_data='scene3')
            markup5.add(markup_start5)
            bot.send_message(callback.message.chat.id, '<i>Поздравление от Ани</i>',
                             parse_mode='html', reply_markup=markup5)
            bot.delete_message(callback.message.chat.id, message.message_id)
    if callback.data == 'scene3':
        with open('IMG_2369.MOV', 'rb') as t:
            message = bot.send_message(callback.message.chat.id, 'Видео загружается...')
            bot.send_video(callback.message.chat.id, t, timeout=50)
            markup6 = types.InlineKeyboardMarkup(row_width=2)
            markup_start6 = types.InlineKeyboardButton(text='Следующее поздравление🎉', callback_data='scene4')
            markup6.add(markup_start6)
            bot.send_message(callback.message.chat.id, '<i>Поздравление от Ани</i>',
                             parse_mode='html', reply_markup=markup6)
            bot.delete_message(callback.message.chat.id, message.message_id)
    if callback.data == 'scene4':
        print('я тут')
        with open('video_2024-02-02_21-16-25.mp4', 'rb') as G:
            message = bot.send_message(callback.message.chat.id, 'Видео загружается...')
            bot.send_video(callback.message.chat.id, G, timeout=50)
            markup7 = types.InlineKeyboardMarkup(row_width=2)
            markup_start7 = types.InlineKeyboardButton(text='Следующее поздравление🎉', callback_data='scene5')
            markup7.add(markup_start7)
            bot.send_message(callback.message.chat.id, '<i>Поздравление от Дани</i>',
                             parse_mode='html', reply_markup=markup7)
            bot.delete_message(callback.message.chat.id, message.message_id)
    if callback.data == 'scene5':
        with open('IMG_1652.MOV', 'rb') as r:
            message = bot.send_message(callback.message.chat.id, 'Видео загружается...')
            bot.send_video(callback.message.chat.id, r, timeout=50)
            markup8 = types.InlineKeyboardMarkup(row_width=2)
            markup_start8 = types.InlineKeyboardButton(text='Следующее поздравление🎉', callback_data='scene6')
            markup8.add(markup_start8)
            bot.send_message(callback.message.chat.id, '<i>Поздравление от Вики</i>',
                             parse_mode='html', reply_markup=markup8)
            bot.delete_message(callback.message.chat.id, message.message_id)
    if callback.data == 'scene6':
        with open('video_2024-02-02_21-19-05.mp4', 'rb') as u:
            message = bot.send_message(callback.message.chat.id, 'Видео загружается...')
            bot.send_video(callback.message.chat.id, u, timeout=50)
            markup81 = types.InlineKeyboardMarkup(row_width=2)
            markup_start81 = types.InlineKeyboardButton(text='Следующее поздравление🎉', callback_data='scene7')
            markup81.add(markup_start81)
            bot.send_message(callback.message.chat.id, '<i>Поздравление от Ромы</i>',
                             parse_mode='html', reply_markup=markup81)
            bot.delete_message(callback.message.chat.id, message.message_id)
    if callback.data == 'scene7':
        print('я тут')
        with open('video_2024-02-02_21-21-38.mp4', 'rb') as l:
            message = bot.send_message(callback.message.chat.id, 'Видео загружается...')
            bot.send_video(callback.message.chat.id, l, timeout=50)
            markup9 = types.InlineKeyboardMarkup(row_width=2)
            markup_start9 = types.InlineKeyboardButton(text='Следующее поздравление🎉', callback_data='scene8')
            markup9.add(markup_start9)
            bot.send_message(callback.message.chat.id, '<i>Поздравление от Кирила</i>',
                             parse_mode='html', reply_markup=markup9)
            bot.delete_message(callback.message.chat.id, message.message_id)
    if callback.data == 'scene8':
        with open('video67.mp4', 'rb') as R:
            message = bot.send_message(callback.message.chat.id, 'Видео загружается...')
            bot.send_video(callback.message.chat.id, R, timeout=50)
            markup10 = types.InlineKeyboardMarkup(row_width=2)
            markup_start10 = types.InlineKeyboardButton(text='Следующее поздравление🎉', callback_data='scene9')
            markup10.add(markup_start10)
            bot.send_message(callback.message.chat.id, '<i>Поздравление от Рашида</i>',
                             parse_mode='html', reply_markup=markup10)
            bot.delete_message(callback.message.chat.id, message.message_id)
    if callback.data == 'scene9':
        with open('IMG_0949.MP4', 'rb') as l:
            message = bot.send_message(callback.message.chat.id, 'Видео загружается...')
            bot.send_video(callback.message.chat.id, l, timeout=50)
            markup11 = types.InlineKeyboardMarkup(row_width=2)
            markup_start11 = types.InlineKeyboardButton(text='Следующее поздравление🎉', callback_data='scene10')
            markup11.add(markup_start11)
            bot.send_message(callback.message.chat.id, '<i>Поздравление от Арины и Вики</i>',
                             parse_mode='html', reply_markup=markup11)
            bot.delete_message(callback.message.chat.id, message.message_id)
    if callback.data == 'scene10':
        with open('IMG_2040.MOV', 'rb') as E:
            message = bot.send_message(callback.message.chat.id, 'Видео загружается...')
            bot.send_video(callback.message.chat.id, E, timeout=50)
            markup12 = types.InlineKeyboardMarkup(row_width=2)
            markup_start12 = types.InlineKeyboardButton(text='Следующее поздравление🎉', callback_data='scene11')
            markup12.add(markup_start12)
            bot.send_message(callback.message.chat.id, '<i>Поздравление от Евгения</i>',
                             parse_mode='html', reply_markup=markup12)
            bot.delete_message(callback.message.chat.id, message.message_id)
    if callback.data == 'scene11':
        with open('IMG_3879.MOV', 'rb') as N:
            message = bot.send_message(callback.message.chat.id, 'Видео загружается...')
            bot.send_video(callback.message.chat.id, N, timeout=50)
            markup13 = types.InlineKeyboardMarkup(row_width=2)
            markup_start13 = types.InlineKeyboardButton(text='Следующее поздравление🎉', callback_data='scene12')
            markup13.add(markup_start13)
            bot.send_message(callback.message.chat.id, '<i>Поздравление от Полины</i>',
                             parse_mode='html', reply_markup=markup13)
            bot.delete_message(callback.message.chat.id, message.message_id)
    if callback.data == 'scene12':
        with open('audio_2024-02-02_21-40-50.ogg', 'rb') as O:
            bot.send_audio(callback.message.chat.id, O)
            markup14 = types.InlineKeyboardMarkup(row_width=2)
            markup_start14 = types.InlineKeyboardButton(text='Следующее поздравление🎉', callback_data='scene13')
            markup14.add(markup_start14)
            bot.send_message(callback.message.chat.id, '<i>Поздравление от Дианы</i>',
                             parse_mode='html', reply_markup=markup14)
    if callback.data == 'scene13':
        with open('audio_2024-02-02_21-43-47.ogg', 'rb') as y:
            bot.send_audio(callback.message.chat.id, y)
            markup15 = types.InlineKeyboardMarkup(row_width=2)
            markup_start15 = types.InlineKeyboardButton(text='Следующее поздравление🎉', callback_data='scene14')
            markup15.add(markup_start15)
            bot.send_message(callback.message.chat.id, '<i>Поздравление от Леры</i>',
                             parse_mode='html', reply_markup=markup15)
    if callback.data == 'scene14':
            markup16 = types.InlineKeyboardMarkup(row_width=2)
            bot.send_message(callback.message.chat.id, '<b>Дорогая Колбун Мария , от лица \n\n</b>'
                                                       '<i>всего ученического состава , \n'
                                                       'хотели бы тебя поздравить с \n'
                                                       'этим счастливым и знаменательным \n'
                                                       'днём в твоей жизни. Ведь в этот \n'
                                                       'день началась именно твоя счастливая \n'
                                                       'история. Когда ты начала впервые \n'
                                                       'говорить , делать первые шаги , \n'
                                                       'ругаться и рости. Мы все смотрели \n'
                                                       'на твои стремления и недуги. \n'
                                                       'Все это мы проживали вместе с \n'
                                                       'тобой , и радовались что ты \n'
                                                       'у нас есть. Вот и прошел еще \n'
                                                       'один год и ты стала мудрее \n'
                                                       'и опытней , 17 лет это не \n'
                                                       'просто цифра , она наполнена \n'
                                                       'моментами , жизнью , переживанием , \n'
                                                       'падениями и победой. Просто всегда \n'
                                                       'счастлива , не опускай рук , иди \n'
                                                       'всегда вперед , люби , мечтай , \n'
                                                       'смейся и жизни. Ведь все в \n'
                                                       'твоих руках !!! \n\n</i>'
                                                       '<b>С ДНЁМ РОЖДЕНИЯ МАШКА !!!!!! 🎊🎁💐🎉</b>', parse_mode='html')
            markup_start16 = types.InlineKeyboardButton(text='Следующее поздравление🎉', callback_data='scene15')
            markup16.add(markup_start16)
            bot.send_message(callback.message.chat.id, '<i>Поздравление от Андрея</i>',
                             parse_mode='html', reply_markup=markup16)
    if callback.data == 'scene15':
        with open('video_2024-02-02_22-05-26.mp4', 'rb') as N:
            with open('video_2024-02-02_22-19-44.mp4', 'rb') as p:
                with open('video_2024-02-02_22-12-56.mp4', 'rb') as b:
                    message = bot.send_message(callback.message.chat.id, 'Видео загружается...')
                    bot.send_video(callback.message.chat.id, N, timeout=50)
                    bot.send_video(callback.message.chat.id, p, timeout=50)
                    bot.send_video(callback.message.chat.id, b, timeout=50)
                    markup17 = types.InlineKeyboardMarkup(row_width=2)
                    markup_start17 = types.InlineKeyboardButton(text='Следующее поздравление🎉', callback_data='scene16')
                    markup17.add(markup_start17)
                    bot.send_message(callback.message.chat.id, '<i>Поздравление от Насти и Ксении\n'
                                                               '(часть 1,2,3)</i>',
                                     parse_mode='html', reply_markup=markup17)
                    bot.delete_message(callback.message.chat.id, message.message_id)
    if callback.data == 'scene16':
        with open('video_2024-02-02_22-27-32.mp4', 'rb') as N1:
            with open('video_2024-02-02_22-31-17.mp4', 'rb') as p2:
                with open('video_2024-02-02_22-31-35.mp4', 'rb') as b1:
                    with open('video_2024-02-02_22-32-01.mp4', 'rb') as i1:
                        with open('video_2024-02-02_22-32-16.mp4', 'rb') as a1:
                            message = bot.send_message(callback.message.chat.id, 'Видео загружается...')
                            bot.send_video(callback.message.chat.id, N1, timeout=120)
                            bot.send_video(callback.message.chat.id, p2, timeout=120)
                            bot.send_video(callback.message.chat.id, b1, timeout=120)
                            bot.send_video(callback.message.chat.id, i1, timeout=120)
                            bot.send_video(callback.message.chat.id, a1, timeout=120)
                            markup18 = types.InlineKeyboardMarkup(row_width=2)
                            markup_start18 = types.InlineKeyboardButton(text='Следующее поздравление🎉', callback_data='scene17')
                            markup18.add(markup_start18)
                            bot.send_message(callback.message.chat.id, '<i>Поздравление от Анжелики\n'
                                                                       '(часть 1,2,3,4,5)</i>',
                                             parse_mode='html', reply_markup=markup18)
                            bot.delete_message(callback.message.chat.id, message.message_id)
    if callback.data == 'scene17':
        with open('audio_2024-02-02_22-49-00.ogg', 'rb') as y:
            bot.send_audio(callback.message.chat.id, y)
            markup19 = types.InlineKeyboardMarkup(row_width=2)
            markup_start19 = types.InlineKeyboardButton(text='Следующее поздравление🎉', callback_data='scene18')
            markup19.add(markup_start19)
            bot.send_message(callback.message.chat.id, '<i>Поздравление от Андрея</i>',
                             parse_mode='html', reply_markup=markup19)
    if callback.data == 'scene18':
        with open('audio_2024-02-02_22-50-19.ogg', 'rb') as y:
            bot.send_audio(callback.message.chat.id, y)
            markup20 = types.InlineKeyboardMarkup(row_width=2)
            markup_start20 = types.InlineKeyboardButton(text='Следующее поздравление🎉', callback_data='scene19')
            markup20.add(markup_start20)
            bot.send_message(callback.message.chat.id, '<i>Поздравление от Валеры</i>',
                             parse_mode='html', reply_markup=markup20)
    if callback.data == 'scene19':
        with open('IMG_6034.MOV', 'rb') as Z:
            message = bot.send_message(callback.message.chat.id, 'Видео загружается...')
            bot.send_video(callback.message.chat.id, Z, timeout=50)
            markup21 = types.InlineKeyboardMarkup(row_width=2)
            markup_start21 = types.InlineKeyboardButton(text='Следующее поздравление🎉', callback_data='scene20')
            markup21.add(markup_start21)
            bot.send_message(callback.message.chat.id, '<i>Поздравление от Славы и Влады</i>',
                             parse_mode='html', reply_markup=markup21)
            bot.delete_message(callback.message.chat.id, message.message_id)
    if callback.data == 'scene20':
        with open('audio_2024-02-02_23-52-11.ogg', 'rb') as y1:
            bot.send_audio(callback.message.chat.id, y1)
            markup22 = types.InlineKeyboardMarkup(row_width=2)
            markup_start22 = types.InlineKeyboardButton(text='Спасибо вам ребята❤️', callback_data='sc')
            markup22.add(markup_start22)
            bot.send_message(callback.message.chat.id, '<i>Поздравление от Сережы</i>',
                             parse_mode='html', reply_markup=markup22)


bot.polling(none_stop=True)