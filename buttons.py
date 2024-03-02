from telebot import types



markup_menu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
menu_btn1 = types.KeyboardButton("Запустить GPT🔥")
menu_btn2 = types.KeyboardButton("👤Профиль")
menu_btn3 = types.KeyboardButton("⚙️Настройки")
markup_menu.add(menu_btn1)
markup_menu.add(menu_btn2, menu_btn3)


markup_promt = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn1 = types.KeyboardButton("Задать вопрос❓")
btn2 = types.KeyboardButton("Продолжить✏️")
btn3 = types.KeyboardButton("Вернуться в меню🏠")
markup_promt.add(btn1, btn2)
markup_promt.add(btn3)


markup_subject = types.InlineKeyboardMarkup(row_width=2)
markup_subject1 = types.InlineKeyboardButton(text='📏Математика', callback_data='subject1')
markup_subject2 = types.InlineKeyboardButton(text='📔Русский язык', callback_data='subject2')
markup_subject3 = types.InlineKeyboardButton(text='🧪Химия', callback_data='subject3')
markup_subject4 = types.InlineKeyboardButton(text='Назад⬅️', callback_data='back')
markup_subject.add(markup_subject1)
markup_subject.add(markup_subject2)
markup_subject.add(markup_subject3)
markup_subject.add(markup_subject4)

markup_level = types.InlineKeyboardMarkup(row_width=2)
markup_level1 = types.InlineKeyboardButton(text='😀Новичок', callback_data='level1')
markup_level2 = types.InlineKeyboardButton(text='🙂Базовый', callback_data='level2')
markup_level3 = types.InlineKeyboardButton(text='😎Профи', callback_data='level3')
markup_level4 = types.InlineKeyboardButton(text='Назад⬅️', callback_data='back')
markup_level.add(markup_level1)
markup_level.add(markup_level2)
markup_level.add(markup_level3)
markup_level.add(markup_level4)



markup = types.ReplyKeyboardRemove()