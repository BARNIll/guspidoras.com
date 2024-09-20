from aiogram import Bot, Dispatcher, executor , types
from aiogram.types.web_app_info import WebAppInfo

bot= Bot('8021502238:AAEduG87dhZtLgST764iCXDw9JKCvoFptAQ')
dp=Dispatcher(bot)


@dp.message_handler(command=['start'])
async def start(message:types.Message)
   markup= types.ReplyKeyboardMarkup
   markup.add(types.ReplyKeyboardButton('Тапать гуся!', web_app=WebAppInfo(url=https://barnill.github.io/gus/)))
    await message.answer ('ТАПАЕШЬ,ТАПАЕШЬ', reply_markup=markup)

executor.start_polling(dp)