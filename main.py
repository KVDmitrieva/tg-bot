import logging
import requests

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode
from aiogram.utils.exceptions import BadRequest

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware


import cnf
import getImage
import myTexts
import creature
import keyboard as kb
from states import States


# log level
logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token=cnf.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

rc = creature.RandomCreature()
gi = getImage.PexelsImages()

@dp.message_handler(state='*', commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.chat.id, myTexts.GREETING)
    await bot.send_message(message.chat.id, myTexts.GET_HELP, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(state='*', commands=['help'])
async def process_help_command(message: types.Message):
    await bot.send_message(message.chat.id, myTexts.HELP, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(state='*',commands=['creature'])
async def process_creature(message: types.Message):
    await bot.send_message(message.chat.id, myTexts.CREATURE)
    choice = rc.get_creatures()
    images = rc.get_photos(choice)
    await bot.send_message(message.chat.id, "Готово!")
    for i in range(3):
        await bot.send_message(message.chat.id, choice[i])
        try:
            await bot.send_photo(message.chat.id, requests.get(images[i]).content)
        except BadRequest:
            await bot.send_message(message.chat.id, myTexts.SORRY)

@dp.message_handler(state='*', commands=['photo'])
async def process_photo_mod(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(States.all()[1])
    await bot.send_message(message.chat.id, myTexts.PHOTO)

@dp.message_handler(state=States.STATE_1)
async def send_photo(message: types.Message):
    key_word = message.text
    if (key_word != 'Еще!') and (key_word != 'Хватит!'):
        gi.find_image(key_word)
    if key_word != 'Хватит!':
        await bot.send_photo(message.chat.id, requests.get(gi.send_image()).content)
        if gi.last:
            await message.reply('Картики кончились(', reply_markup=kb.photo_kb2, reply=False)
        else:
            await message.reply('Еще?', reply_markup=kb.photo_kb1, reply=False)
    if key_word == 'Хватит!':
        await message.reply("Все, я закончил", reply_markup=kb.ReplyKeyboardRemove(), reply=False)
        state = dp.current_state(user=message.from_user.id)
        await state.set_state(States.STATE_0)

async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
