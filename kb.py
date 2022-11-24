from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

fkb = InlineKeyboardMarkup(row_width=1)
anxiety = InlineKeyboardButton(text='Мне тревожно 😰', callback_data='anxiety_cb') 
fkb.add(anxiety)

lvl_of_anxiety = InlineKeyboardMarkup(row_width=5)

lvl_1 = InlineKeyboardButton(text='1',callback_data='lvl1')
lvl_2 = InlineKeyboardButton(text='2',callback_data='lvl2')
lvl_3 = InlineKeyboardButton(text='3',callback_data='lvl3')
lvl_4 = InlineKeyboardButton(text='4',callback_data='lvl4')
lvl_5 = InlineKeyboardButton(text='5',callback_data='lvl5')
lvl_6 = InlineKeyboardButton(text='6',callback_data='lvl6')
lvl_7 = InlineKeyboardButton(text='7',callback_data='lvl7')
lvl_8 = InlineKeyboardButton(text='8',callback_data='lvl8')
lvl_9 = InlineKeyboardButton(text='9',callback_data='lvl9')
lvl_10 = InlineKeyboardButton(text='10',callback_data='lvl10')

# lvl_of_anxiety.add(lvl_1,lvl_2,lvl_3,lvl_4,lvl_5)
lvl_of_anxiety.row(lvl_1,lvl_2,lvl_3,lvl_4,lvl_5)
# lvl_of_anxiety.add(lvl_6,lvl_7,lvl_8,lvl_9,lvl_10)
lvl_of_anxiety.row(lvl_6,lvl_7,lvl_8,lvl_9,lvl_10)

complete = InlineKeyboardMarkup()
complete_btn = InlineKeyboardButton(text="Я выполнил тренинг 🏆", callback_data='compl')
complete.add(complete_btn)

menus = InlineKeyboardMarkup()
menus_btn = InlineKeyboardButton(text='Вернуться назад в меню',callback_data='menu')
menus.add(menus_btn)

finish = InlineKeyboardMarkup(row_width=1)
finish_btn_1 = InlineKeyboardButton(text='Мне нужен другой уровень😥', callback_data='otherlvl')
finish_btn_2 = InlineKeyboardButton(text='Оставить отзыв💬', callback_data='feedback')
finish.add(finish_btn_1)
finish.insert(finish_btn_2)
finish.insert(menus_btn)
