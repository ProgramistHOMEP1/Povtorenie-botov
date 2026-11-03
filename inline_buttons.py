from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Математика", callback_data="btn1", style="success"),
        InlineKeyboardButton(text="Русский", callback_data="btn2", style="primary")
    ],
    [
        InlineKeyboardButton(text="Главное меню", callback_data="btn3", style="danger")
    ]
])