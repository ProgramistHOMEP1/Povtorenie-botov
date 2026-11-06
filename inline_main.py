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
from inline_buttons import math_inline_keyboard



load_dotenv()
mytoken = os.getenv("TOKEN")

mybot = Bot(token=mytoken) 
mydispatcher = Dispatcher()
dp = Dispatcher(storage=MemoryStorage())


class States(StatesGroup):
    first_number = State()
    second_number = State()
    minus_first_number = State()
    minus_second_number = State()







async def main():
    await mydispatcher.start_polling(mybot)


@mydispatcher.message(F.text=="/start")
async def command_start(message: Message) -> None:
    await message.answer(f"Добро пожаловать в бота, {message.from_user.first_name}", reply_markup=main_inline_keyboard)
    await message.delete()


@mydispatcher.callback_query(F.data == "btnmain")
async def handle_btn1(callback: CallbackQuery):
    await callback.answer("Нажата кнопка ГЛАВНОЕ МЕНЮ")
    await callback.message.edit_text(f" Вы в главном меню, {callback.from_user.first_name}", reply_markup=main_inline_keyboard)



@mydispatcher.callback_query(F.data == "btnmath")
async def handle_btn1(callback: CallbackQuery):
    await callback.answer("Нажата кнопка 1")
    await callback.message.edit_text(f"Добро пожаловать в бота, {callback.from_user.first_name}", reply_markup=math_inline_keyboard)



@mydispatcher.callback_query(F.data == "btnplus")
async def handle_btn1(callback: CallbackQuery, state: FSMContext):
    await callback.answer("Нажата кнопка ПЛЮС")
    await callback.message.answer("Введите первое число:", reply_markup=math_inline_keyboard)
    await state.set_state(States.first_number)

@mydispatcher.message(States.first_number)
async def command_start(message: Message, state: FSMContext) -> None:
    await message.answer(f"Отлично, теперь напиши второе число:", reply_markup=math_inline_keyboard)
    await state.update_data(number=message.text)
    await state.set_state(States.second_number)


@mydispatcher.message(States.second_number)
async def command_start(message: Message, state: FSMContext) -> None:
    temp_data = await state.get_data()
    await message.answer(f"Результат сложения ваших чисел: {int(temp_data['number'])+int(message.text)}", reply_markup=math_inline_keyboard)
    await state.clear()  



@mydispatcher.callback_query(F.data == "btnmathminus")
async def handle_btn1(callback: CallbackQuery):
    await callback.answer("Нажата кнопка МИНУС")
    await callback.message.answer("Введите первое число:", reply_markup=math_inline_keyboard)



# Домашнее задание:

# Аналогично кнопке "+" сделать кнопку "-". Последовательно спрашивать два числа и выдавать результат их разницу




























if __name__ == "__main__":
    asyncio.run(main())