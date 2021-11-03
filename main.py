from aiogram import Bot, Dispatcher, executor, types
import asyncio
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InputFile
from keyboard import *
api = '1949798555:AAEI76epvCeDOaU0UdOilg3Cz60ED8vIF9I'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kolvo_good = 0

@dp.message_handler(commands='start')
async def starter(message: types.Message):
	start_photo = InputFile('Ptest.jpg')
	name = message['from']
	await message.answer(f'Добро пожаловать, {name["first_name"]}! Предлагаю пройти тест и узнать насколько хорошо ты знаешь основы языка программирования Python')
	await message.answer('ПРИМЕЧАНИЕ: Перед повторным запуском, необходимо пройти тест полностью!')
	await bot.send_photo(chat_id=message.chat.id, photo=start_photo, reply_markup=start_menu)

users = {}
@dp.callback_query_handler(text_contains='go')
async def fff(callback_query: types.CallbackQuery):
	global users
	id = callback_query['from']['id']
	users[id] = 0
	first_photo = InputFile('vopros1.jpg')
	await bot.send_message(callback_query.from_user.id, 'Превый вопрос. Что напечатает следующий код?')
	await bot.send_photo(callback_query.from_user.id, photo=first_photo, reply_markup=first_menu)


@dp.callback_query_handler(text_contains='1well')
async def fff(callback_query: types.CallbackQuery):
	global users
	id = callback_query['from']['id']
	if users[id] == 0:
		users[id] = 1
		global kolvo_good
		kolvo_good += 1
		await bot.answer_callback_query(callback_query.id, text='Верно!', show_alert=True)
		second_photo = InputFile('vopros2.jpg')
		await bot.send_message(callback_query.from_user.id, 'Переходим ко второму вопросу. Что напечатает следующий код?')
		await bot.send_photo(callback_query.from_user.id, photo=second_photo, reply_markup=second_menu)
	else:
		pass

@dp.callback_query_handler(text_contains='1')
async def fff(callback_query: types.CallbackQuery):
	global users
	id = callback_query['from']['id']
	if users[id] == 0:
		users[id] = 1
		await bot.answer_callback_query(callback_query.id, text='Неверно:(', show_alert=True)
		second_photo = InputFile('vopros2.jpg')
		await bot.send_message(callback_query.from_user.id, 'Переходим ко второму вопросу. Что напечатает следующий код?')
		await bot.send_photo(callback_query.from_user.id, photo=second_photo, reply_markup=second_menu)
	else:
		pass

@dp.callback_query_handler(text_contains='2well')
async def fff(callback_query: types.CallbackQuery):
	global users
	id = callback_query['from']['id']
	if users[id] == 1:
		users[id] = 2
		global kolvo_good
		kolvo_good += 1
		await bot.answer_callback_query(callback_query.id, text='Верно!', show_alert=True)
		await bot.send_message(callback_query.from_user.id, 'Время третьего вопроса. Что отвечает за создание функции?', reply_markup=third_menu)
	else:
		pass

@dp.callback_query_handler(text_contains='2')
async def fff(callback_query: types.CallbackQuery):
	global users
	id = callback_query['from']['id']
	if users[id] == 1:
		users[id] = 2
		await bot.answer_callback_query(callback_query.id, text='Неверно:(', show_alert=True)
		await bot.send_message(callback_query.from_user.id, 'Время третьего вопроса. Что отвечает за создание функции?', reply_markup=third_menu)
	else:
		pass

@dp.callback_query_handler(text_contains='3well')
async def fff(callback_query: types.CallbackQuery):
	global users
	id = callback_query['from']['id']
	if users[id] == 2:
		users[id] = 3
		global kolvo_good
		kolvo_good += 1
		await bot.answer_callback_query(callback_query.id, text='Верно!', show_alert=True)
		fourth_photo = InputFile('vopros4.jpg')
		await bot.send_message(callback_query.from_user.id, 'Переходим к четвертому вопросу. Что напечатает следующий код?')
		await bot.send_photo(callback_query.from_user.id, photo=fourth_photo, reply_markup=fourth_menu)
	else:
		pass

@dp.callback_query_handler(text_contains='3')
async def fff(callback_query: types.CallbackQuery):
	global users
	id = callback_query['from']['id']
	if users[id] == 2:
		users[id] = 3
		await bot.answer_callback_query(callback_query.id, text='Неверно(', show_alert=True)
		fourth_photo = InputFile('vopros4.jpg')
		await bot.send_message(callback_query.from_user.id, 'Переходим к четвертому вопросу. Что напечатает следующий код?')
		await bot.send_photo(callback_query.from_user.id, photo=fourth_photo, reply_markup=fourth_menu)
	else:
		pass

@dp.callback_query_handler(text_contains='4well')
async def fff(callback_query: types.CallbackQuery):
	global users
	id = callback_query['from']['id']
	if users[id] == 3:
		users[id] = 4
		global kolvo_good
		kolvo_good += 1
		await bot.answer_callback_query(callback_query.id, text='Верно!', show_alert=True)
		fifth_photo = InputFile('vopros5.jpg')
		await bot.send_message(callback_query.from_user.id, 'Переходим к пятому вопросу. Что напечатает следующий код?')
		await bot.send_photo(callback_query.from_user.id, photo=fifth_photo, reply_markup=fifth_menu)
	else:
		pass

@dp.callback_query_handler(text_contains='4')
async def fff(callback_query: types.CallbackQuery):
	global users
	id = callback_query['from']['id']
	if users[id] == 3:
		users[id] = 4
		await bot.answer_callback_query(callback_query.id, text='Неверно(', show_alert=True)
		fifth_photo = InputFile('vopros5.jpg')
		await bot.send_message(callback_query.from_user.id, 'Переходим к пятому вопросу. Что напечатает следующий код?')
		await bot.send_photo(callback_query.from_user.id, photo=fifth_photo, reply_markup=fifth_menu)
	else:
		pass

@dp.callback_query_handler(text_contains='5well')
async def fff(callback_query: types.CallbackQuery):
	global users
	id = callback_query['from']['id']
	if users[id] == 4:
		users[id] = 5
		global kolvo_good
		kolvo_good += 1
		await bot.answer_callback_query(callback_query.id, text='Верно!', show_alert=True)
		sixth_photo = InputFile('vopros6.jpg')
		await bot.send_message(callback_query.from_user.id, 'Переходим к шестому вопросу. Что напечатает следующий код?')
		await bot.send_photo(callback_query.from_user.id, photo=sixth_photo, reply_markup=sixth_menu)
	else:
		pass

@dp.callback_query_handler(text_contains='5')
async def fff(callback_query: types.CallbackQuery):
	global users
	id = callback_query['from']['id']
	if users[id] == 4:
		users[id] = 5
		await bot.answer_callback_query(callback_query.id, text='Неверно(', show_alert=True)
		sixth_photo = InputFile('vopros6.jpg')
		await bot.send_message(callback_query.from_user.id, 'Переходим к шестому вопросу. Что напечатает следующий код?')
		await bot.send_photo(callback_query.from_user.id, photo=sixth_photo, reply_markup=sixth_menu)
	else:
		pass

@dp.callback_query_handler(text_contains='6well')
async def fff(callback_query: types.CallbackQuery):
	global users
	id = callback_query['from']['id']
	if users[id] == 5:
		users[id] = 6
		global kolvo_good
		kolvo_good += 1
		await bot.answer_callback_query(callback_query.id, text='Верно!', show_alert=True)
		seventh_photo = InputFile('vopros7.jpg')
		await bot.send_message(callback_query.from_user.id, 'Время седьмого вопроса. Что напечатает следующий код?')
		await bot.send_photo(callback_query.from_user.id, photo=seventh_photo, reply_markup=seventh_menu)
	else:
		pass

@dp.callback_query_handler(text_contains='6')
async def fff(callback_query: types.CallbackQuery):
	global users
	id = callback_query['from']['id']
	if users[id] == 5:
		users[id] = 6
		await bot.answer_callback_query(callback_query.id, text='Неверно(', show_alert=True)
		seventh_photo = InputFile('vopros7.jpg')
		await bot.send_message(callback_query.from_user.id, 'Время седьмого вопроса. Что напечатает следующий код?')
		await bot.send_photo(callback_query.from_user.id, photo=seventh_photo, reply_markup=seventh_menu)
	else:
		pass

@dp.callback_query_handler(text_contains='7well')
async def fff(callback_query: types.CallbackQuery):
	global users
	id = callback_query['from']['id']
	if users[id] == 6:
		users[id] = 7
		global kolvo_good
		kolvo_good += 1
		await bot.answer_callback_query(callback_query.id, text='Верно!', show_alert=True)
		eighth_photo = InputFile('vopros8.jpg')
		await bot.send_message(callback_query.from_user.id, 'Переходим к восьмому вопросу. Что напечатает следующий код?')
		await bot.send_photo(callback_query.from_user.id, photo=eighth_photo, reply_markup=eighth_menu)
	else:
		pass

@dp.callback_query_handler(text_contains='7')
async def fff(callback_query: types.CallbackQuery):
	global users
	id = callback_query['from']['id']
	if users[id] == 6:
		users[id] = 7
		await bot.answer_callback_query(callback_query.id, text='Неверно(', show_alert=True)
		eighth_photo = InputFile('vopros8.jpg')
		await bot.send_message(callback_query.from_user.id, 'Переходим к восьмому вопросу. Что напечатает следующий код?')
		await bot.send_photo(callback_query.from_user.id, photo=eighth_photo, reply_markup=eighth_menu)
	else:
		pass

@dp.callback_query_handler(text_contains='8well')
async def fff(callback_query: types.CallbackQuery):
	global users
	id = callback_query['from']['id']
	if users[id] == 7:
		users[id] = 8
		global kolvo_good
		kolvo_good += 1
		await bot.answer_callback_query(callback_query.id, text='Верно!', show_alert=True)
		ninth_photo = InputFile('vopros9.jpg')
		await bot.send_message(callback_query.from_user.id, 'Переходим к девятому вопросу. Что напечатает следующий код?')
		await bot.send_photo(callback_query.from_user.id, photo=ninth_photo, reply_markup=ninth_menu)
	else:
		pass

@dp.callback_query_handler(text_contains='8')
async def fff(callback_query: types.CallbackQuery):
	global users
	id = callback_query['from']['id']
	if users[id] == 7:
		users[id] = 8
		await bot.answer_callback_query(callback_query.id, text='Неверно(', show_alert=True)
		ninth_photo = InputFile('vopros9.jpg')
		await bot.send_message(callback_query.from_user.id, 'Переходим к девятому вопросу. Что напечатает следующий код?')
		await bot.send_photo(callback_query.from_user.id, photo=ninth_photo, reply_markup=ninth_menu)
	else:
		pass

@dp.callback_query_handler(text_contains='9well')
async def fff(callback_query: types.CallbackQuery):
	global users
	id = callback_query['from']['id']
	if users[id] == 8:
		users[id] = 9
		global kolvo_good
		kolvo_good += 1
		await bot.answer_callback_query(callback_query.id, text='Верно!', show_alert=True)
		tenth_photo = InputFile('vopros10.jpg')
		await bot.send_message(callback_query.from_user.id, 'Десятый вопрос - заключительный! Что напечатает следующий код?')
		await bot.send_photo(callback_query.from_user.id, photo=tenth_photo, reply_markup=tenth_menu)
	else:
		pass

@dp.callback_query_handler(text_contains='9')
async def fff(callback_query: types.CallbackQuery):
	global users
	id = callback_query['from']['id']
	if users[id] == 8:
		users[id] = 9
		await bot.answer_callback_query(callback_query.id, text='Неверно(', show_alert=True)
		tenth_photo = InputFile('vopros10.jpg')
		await bot.send_message(callback_query.from_user.id, 'Десятый вопрос - заключительный! Что напечатает следующий код?')
		await bot.send_photo(callback_query.from_user.id, photo=tenth_photo, reply_markup=tenth_menu)
	else:
		pass

@dp.callback_query_handler(text_contains='-well')
async def fff(callback_query: types.CallbackQuery):
	global users
	id = callback_query['from']['id']
	if users[id] == 9:
		users[id] = 0
		global kolvo_good
		kolvo_good += 1
		await bot.answer_callback_query(callback_query.id, text='Верно!', show_alert=True)
		await bot.send_message(callback_query.from_user.id, f'Тест пройден! Вы набрали {kolvo_good} очков!')
		if kolvo_good <= 5:
			await bot.send_message(callback_query.from_user.id, 'https://easypro.academy/kursy-programmirovaniya-dlya-detej/  - это материалы, по которым можно подтянуть свои знания!')
		else:
			await  bot.send_message(callback_query.from_user.id, 'Молодец, так держать! https://easypro.academy/kursy-programmirovaniya-dlya-detej/  - это материалы, по которым Вы сможете продолжить изучение Python!')
	else:
		pass

@dp.callback_query_handler(text_contains='-')
async def fff(callback_query: types.CallbackQuery):
	global users
	id = callback_query['from']['id']
	if users[id] == 9:
		users[id] = 0
		await bot.answer_callback_query(callback_query.id, text='Неверно(', show_alert=True)
		await bot.send_message(callback_query.from_user.id, f'Тест пройден! Вы набрали {kolvo_good} очков!')
		if kolvo_good <= 5:
			await bot.send_message(callback_query.from_user.id, 'https://easypro.academy/kursy-programmirovaniya-dlya-detej/  - это материалы, по которым можно подтянуть свои знания')
		else:
			await  bot.send_message(callback_query.from_user.id, 'Молодец, так держать!  https://easypro.academy/kursy-programmirovaniya-dlya-detej/  - это материалы, по которым Вы сможете продолжить изучение Python!')
	else:
		pass

@dp.message_handler()
async def fff(message: types.Message):
	await message.answer('Я Вас не понимаю. Обратитесь, пожалуйста, к администратору', reply_markup= admin_menu)



if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	executor.start_polling(dp)
