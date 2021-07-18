from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup


button_stop = 'Хватит!'
button_next = 'Еще!'

photo_kb1 = ReplyKeyboardMarkup(
                resize_keyboard=True,
                one_time_keyboard=True).row(button_stop, button_next)
photo_kb2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_stop)
