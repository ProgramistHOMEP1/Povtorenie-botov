from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_buttons = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[
[KeyboardButton(text="Математика", style="primary"),KeyboardButton(text="Русский", style="danger")],


])

math_buttons = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[
[KeyboardButton(text="Плюс", style="primary"), KeyboardButton(text="Минус", style="success"), KeyboardButton(text="Умножить", style="danger")],
[KeyboardButton(text="Главное меню")]


])

russian_buttons = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[
[KeyboardButton(text="Текст", style="primary")],
[KeyboardButton(text="Главное меню")]


])