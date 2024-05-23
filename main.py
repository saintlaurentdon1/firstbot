from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
bot = Bot(token=  '6968625615:AAF-42er31AnyT3XSoP7HZUGmlkvSmPdIcw')
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard= True)
button = KeyboardButton('Клик')
button1 = KeyboardButton('Клик-клик')
keyboard.add(button,button1)

keyboard_2 = ReplyKeyboardMarkup(resize_keyboard= True)
button_3 = KeyboardButton('Клик')
button_4 = KeyboardButton('Вернуться на первую клавиатуру')
keyboard_2.add(button_3,button_4)


keyboard_Inline = InlineKeyboardMarkup(row_width= 2)
button_Inline = InlineKeyboardButton('Покажи гугл браузер', url='https://www.google.com/')
button_Inline1 = InlineKeyboardButton('Покажи яндекс браузер', url='https://ya.ru/?utm_referrer=https%3A%2F%2Fwww.google.com%2F')
keyboard_Inline.add(button_Inline, button_Inline1)
async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Команда для того, чтобы запустить бота'),

    ]

    await bot.set_my_commands(commands)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, я твой первый ЭХО бот', reply_markup= keyboard)

@dp.message_handler(lambda message: message.text == 'Клик')
async def button_click(message: types.Message):
    await message.answer('Браузеры', reply_markup= keyboard_Inline)

@dp.message_handler(lambda message: message.text == 'Клик-клик')
async def button1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://i.pinimg.com/736x/3e/e7/f1/3ee7f107f4c8633d370a4b86101a4958.jpg', caption= 'свинка!!')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)