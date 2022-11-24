from aiogram import types
from aiogram import asyncio
from aiogram.types import Message, CallbackQuery, MediaGroup, InputFile, LabeledPrice, PreCheckoutQuery
from aiogram.dispatcher.filters import Command
from aiogram.types.message import ContentType
from kb import *
import aioschedule as schedule
from datetime import datetime, timedelta, timezone
import random

from main import dp,bot

import sqlite3


list_lvl_1_4 = ["Упражнение <b>Дневник</b>\n\nПростой и очень эффективный способ.\nВозьми бумагу и ручку. Если под рукой только телефон можно писать в нем. Поставь таймер на 15 минут. Выпиши из головы всё, что тебя тревожит и причиняет беспокойство.\n\nСолнышко, когда ты все доделаешь, пожалуйста, нажми на кнопочку снизу"]
list_lvl_5_7 = ["Упражнение <b>Центрирование</b>\n\nДля устойчивости и связи со своим телом. Тревога вызывает в теле напряжение и зажатость. Сегодня мы через тело будем учиться выходить из этого напряжения.\n\nПослушай аудио.","Упражнение <b>Самый худший сценарий</b>\n\nТебе понадобятся листок и ручка. Если под рукой только телефон, можешь писать в заметки.\nУпражнение состоит из 2 частей.\n\n1. Подумай о ситуации, которая тебя тревожит. Представь самый худший сценарий из возможных. Самый худший. Сгущай краски. Подробно запиши его.\n2. Теперь запиши свой план - что ты будешь делать в этой ситуации.\nТеперь у тебя есть план на самый худший вариант развития события. Скорее всего, он не произойдет - обычно страшные картины нашего воображения не воплощаются в жизнь. Но даже если это будет исключение - ты знаешь, что делать.\n\nСолнышко, когда ты все доделаешь, пожалуйста, нажми на кнопочку снизу"]
list_lvl_8_10 = ["Упражнение <b>Дыхание 3-5-2</b>\n\nНаша задача - снизить тревогу. Дыхательные техники - один из самых эффективных способов.\nПоставь таймер на 4 минуты и дыши это время по схеме: вдох на 3 счёта - выдох на 5 счетов - пауза на 2 счета.\nПослушай аудио.\n\nСолнышко, когда ты все доделаешь, пожалуйста, нажми на кнопочку снизу","Упражнение <b>Физическая разрядка</b>\n\nЕсли тебе есть, где уединиться и шум не вызовет вопросов – потопай ногами. Сильно, интенсивно потопай ногами 50 раз. Небольшой перерыв, отдышись и ещё потопай ещё 50 раз, часто перебирая ногами.\nЕсли такой возможности нет, сильно сожми кулаки обеих рук и подержи 3 секунды. Расслабь. Снова сожми и 3 секунды держи сжатыми. Расслабь. Сделай так 50 раз.\n\nСолнышко, когда ты все доделаешь, пожалуйста, нажми на кнопочку снизу"]



@dp.message_handler(Command('start'))
async def start(message: Message):
    await message.answer('Привет, мой дорогой друг!\nМеня зовут <b>Calmly</b>, я помогу тебе справится со стрессом и тревогой\nНажимай на кнопочки снизу и мы все решим\n', reply_markup=fkb)
    connect = sqlite3.connect('calmly.db')
    cursor = connect.cursor()
    if cursor.execute("SELECT * FROM users WHERE user_id = ?", (message.chat.id,)).fetchone() == None:
        cursor.execute("INSERT INTO users (user_id, name) VALUES (?, ?)", [message.chat.id, message.chat.first_name])
        cursor.close()
        connect.commit()
        connect.close()
    else:
        cursor.close()
        connect.commit()
        connect.close()

@dp.message_handler(Command('admin'))
async def adm(message:Message):
    await bot.send_message(message.chat.id,"Давай я помогу тебе!\nПожалуйста, выбери свой уровень тревожности от 1 до 10\nЖми на кнопочку снизу", reply_markup=lvl_of_anxiety)       

@dp.callback_query_handler(text='anxiety_cb')
async def anxiety_cb(call:types.callback_query):
    await call.message.edit_text("Давай я помогу тебе!\nПожалуйста, выбери свой уровень тревожности от 1 до 10\nЖми на кнопочку снизу", reply_markup=lvl_of_anxiety)

@dp.callback_query_handler(text='lvl1')
async def lvl1(call:types.callback_query):
    await call.message.edit_text(random.choice(list_lvl_1_4), reply_markup = complete)

@dp.callback_query_handler(text='lvl2')
async def lvl1(call:types.callback_query):
    await call.message.edit_text("Упражнение <b>Дневник</b>\n\nПростой и очень эффективный способ.\nВозьми бумагу и ручку. Если под рукой только телефон можно писать в нем. Поставь таймер на 15 минут. Выпиши из головы всё, что тебя тревожит и причиняет беспокойство.\nСолнышко, когда ты все доделаешь, пожалуйста, нажми на кнопочку снизу", reply_markup = complete)

@dp.callback_query_handler(text='lvl3')
async def lvl1(call:types.callback_query):
    await call.message.edit_text("Упражнение <b>Дневник</b>\n\nПростой и очень эффективный способ.\nВозьми бумагу и ручку. Если под рукой только телефон можно писать в нем. Поставь таймер на 15 минут. Выпиши из головы всё, что тебя тревожит и причиняет беспокойство.\nСолнышко, когда ты все доделаешь, пожалуйста, нажми на кнопочку снизу", reply_markup = complete)

@dp.callback_query_handler(text='lvl4')
async def lvl1(call:types.callback_query):
    await call.message.edit_text("Упражнение <b>Дневник</b>\n\nПростой и очень эффективный способ.\nВозьми бумагу и ручку. Если под рукой только телефон можно писать в нем. Поставь таймер на 15 минут. Выпиши из головы всё, что тебя тревожит и причиняет беспокойство.\nСолнышко, когда ты все доделаешь, пожалуйста, нажми на кнопочку снизу", reply_markup = complete)

    
@dp.callback_query_handler(text='lvl5')
async def lvl1(call:types.callback_query):
    t = random.choice(list_lvl_5_7)
    if t[14] == 'Ц':
        with open('center.mp3','rb') as f:
            cont1 = f.read()
            Title1 = 'Центрирование'
    await bot.send_audio(call.message.chat.id, audio=cont1, performer = 'Упражнение', title=Title1)
    await call.message.edit_text(t, reply_markup = complete)

@dp.callback_query_handler(text='lvl6')
async def lvl1(call:types.callback_query):
    t = random.choice(list_lvl_5_7)
    if t[14] == 'Ц':
        with open('center.mp3','rb') as f:
            cont1 = f.read()
            Title1 = 'Центрирование'
    await bot.send_audio(call.message.chat.id, audio=cont1, performer = 'Упражнение', title=Title1)
    await call.message.edit_text(t, reply_markup = complete)

@dp.callback_query_handler(text='lvl7')
async def lvl1(call:types.callback_query):
    t = random.choice(list_lvl_5_7)
    if t[14] == 'Ц':
        with open('center.mp3','rb') as f:
            cont1 = f.read()
            Title1 = 'Центрирование'
        await bot.send_audio(call.message.chat.id, audio=cont1, performer = 'Упражнение', title=Title1)
    await call.message.edit_text(t, reply_markup = complete)



@dp.callback_query_handler(text='lvl8')
async def lvl1(call:types.callback_query):
    a = random.choice(list_lvl_8_10)
    if a[14] == 'Д':
        with open('breath.mp3','rb') as f:
            cont = f.read()
            Title = "Дыхание 3-5-2"
    # elif a[14] == 'Ф':
    #     with open('center.mp3','rb') as f:
    #         cont = f.read()
    #         Title = 'Центрирование'
        await bot.send_audio(call.message.chat.id, audio=cont, performer = 'Упражнение', title=Title)
    await call.message.edit_text(a, reply_markup = complete)

@dp.callback_query_handler(text='lvl9')
async def lvl1(call:types.callback_query):
    a = random.choice(list_lvl_8_10)
    if a[14] == 'Д':
        with open('breath.mp3','rb') as f:
            cont = f.read()
            Title = "Дыхание 3-5-2"
    # elif a[14] == 'Ф':
        # with open('center.mp3','rb') as f:
        #     cont = f.read()
        #     Title = 'Центрирование'
        await bot.send_audio(call.message.chat.id, audio=cont, performer = 'Упражнение', title=Title)
    await call.message.edit_text(a, reply_markup = complete)

@dp.callback_query_handler(text='lvl10')
async def lvl1(call:types.callback_query):
    a = random.choice(list_lvl_8_10)
    if a[14] == 'Д':
        with open('breath.mp3','rb') as f:
            cont = f.read()
            Title = "Дыхание 3-5-2"
    # elif a[14] == 'Ф':
        # with open('center.mp3','rb') as f:
            # cont = f.read()
            # Title = 'Центрирование'
        await bot.send_audio(call.message.chat.id, audio=cont, performer = 'Упражнение', title=Title)
    await call.message.edit_text(a, reply_markup = complete)


    



@dp.callback_query_handler(text='compl')
async def compls(call:types.callback_query):
    await call.message.delete()
    await bot.send_message(call.message.chat.id,"Ты большой молодец!\nЯ скоро вернусь и узнаю, как ты себя чувствуешь!")
    await asyncio.sleep(30)
    await bot.send_message(call.message.chat.id, "Как ты тут?\nЕсли все прошло хорошо, то ты можешь оставить отзыв\nА если тревога не ушла, попробуй тренинг для более высокого уровня", reply_markup=finish)

@dp.callback_query_handler(text = 'otherlvl')
async def other(call:types.callback_query):
    await call.message.edit_text("Давай я помогу тебе!\nПожалуйста, выбери свой уровень тревожности от 1 до 10\nЖми на кнопочку снизу", reply_markup=lvl_of_anxiety)

@dp.callback_query_handler(text = 'feedback')
async def feed(call:types.callback_query):
    await call.message.edit_text("Я была рада тебе помочь!\nНапиши свой отзыв следующим сообщением и я доставлю его Саше")
    
    @dp.message_handler()
    async def feedback(message: types.Message):
        await bot.send_message(call.message.chat.id,"Твой отзыв успешно доставлен)")
        await bot.forward_message(481608826, message.from_user.id, message.message_id)
    
@dp.callback_query_handler(text='menu')
async def menu(call:types.callback_query):
    await call.message.edit_text('Привет, мой дорогой друг!\nМеня зовут <b>Calmly</b>, я помогу тебе справится со стрессом и тревогой\nНажимай на кнопочки снизу и мы все решим\n', reply_markup=fkb)