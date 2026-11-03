import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from dotenv import load_dotenv
import os
from buttons import main_buttons, math_buttons, russian_buttons
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from inline_buttons import main_inline_keyboard
from aiogram.types import CallbackQuery


load_dotenv()
mytoken = os.getenv("TOKEN")

mybot = Bot(token=mytoken) 
mydispatcher = Dispatcher()
dp = Dispatcher(storage=MemoryStorage())


async def main():
    await mydispatcher.start_polling(mybot)


@mydispatcher.message(F.text=="/start")
async def command_start(message: Message) -> None:
    await message.answer("Добро пожаловать в бота, {message.from_user.first_name}", reply_markup=main_inline_keyboard)


@mydispatcher.callback_query(F.data == "btn1")
async def handle_btn1(callback: CallbackQuery):
    await callback.answer("Нажата кнопка 1")
    await callback.message.answer("Обратное сообщение")