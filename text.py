
def Greeting(name):
    text = ( f'<b>Привет {name}👋,\n</b>'
          f'<i>Я нейросеть и я могу\n'
          f'рассказать и обьяснить\n'
          f'школьные предметы,\n'
          f'как новичку так и профи.\n\n</i>'
          f'<b>P.S Пиши свой промт \n'
          f'корректно и понятно.\n</b>',)
    return text


def Profile(name, sub, lev, req):
    info = ('<b>Твой профиль👤\n\n</b>'
              f'<b>Имя:</b> {name}\n'
              f'<b>Предмет:</b> {sub}\n'
              f'<b>Уровень:</b> {lev}\n'
              f'<b>Кол-запросов:</b> {req}\n'
              '<b>Язык общения:</b> Русский\n\n'
              '<b>Примечание: \n</b>'
              '<i>Если вы не настроите GPT\n'
              'под себя, ваши настройки \n'
              'по умолчанию будут</i> <b>"математика\n'
              'с базовым уровнем"</b>.')
    return info


def answer(question1, result):
    answer1 = ('<b>Твой вопрос: \n</b>'
                f'<i>{question1}</i>\n'
                f'<b>Ответ:\n</b>'
                f'<i>{result.text}</i>')
    return answer1