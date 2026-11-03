from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Математика", callback_data="btnmath", style="success"),
        InlineKeyboardButton(text="Русский", callback_data="btnrussian", style="primary")
    ],
])



math_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Плюс", callback_data="btnplus", style="success"),
        InlineKeyboardButton(text="Минус", callback_data="btnminus", style="primary")
    ],
    [
        InlineKeyboardButton(text="Главное меню", callback_data="btnmain", style="danger")
    ]
])