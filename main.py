import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from dotenv import load_dotenv
import os
from buttons import main_buttons, math_buttons, russian_buttons
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


load_dotenv()
mytoken = os.getenv("TOKEN")

mybot = Bot(token=mytoken) 
mydispatcher = Dispatcher()
dp = Dispatcher(storage=MemoryStorage())

class States(StatesGroup):
    first_number = State()
    second_number = State()





async def main():
    await mydispatcher.start_polling(mybot)


@mydispatcher.message(F.text=="/start")
async def command_start(message: Message) -> None:
    await message.answer(f"Привет, {message.from_user.first_name}", reply_markup=main_buttons)
    


@mydispatcher.message(F.text=="/donat")
async def command_start(message: Message) -> None:
    await message.answer(f"{message.from_user.first_name}, Вы хотите сделать донат?\n Реквизиты для доната: +5674986587 Ульфа-Банк")
    

@mydispatcher.message(F.text.startswith("/better "))
async def command_age(message):
    newtext = message.text.split(" ")
    if int(newtext[1])>int(newtext[2]):
        await message.answer(f"Число {newtext[1]} больше!")
    if int(newtext[2])>int(newtext[1]):
        await message.answer(f"Число {newtext[2]} больше!")
    if int(newtext[1])==int(newtext[2]):
        await message.answer(f"Число ваши числа одинаковые!")


@mydispatcher.message(F.text=="Математика")
async def command_start(message: Message) -> None:
    await message.answer(f"Математика", reply_markup=math_buttons)
    

@mydispatcher.message(F.text=="Русский")
async def command_start(message: Message) -> None:
    await message.answer(f"Русский", reply_markup=russian_buttons)
    




@mydispatcher.message(F.text=="Плюс")
async def command_start(message: Message, state: FSMContext) -> None:
    await message.answer(f"Тест кнопки ПЛЮС", reply_markup=math_buttons)
    await state.set_state(States.first_number)

@mydispatcher.message(States.first_number)
async def command_start(message: Message, state: FSMContext) -> None:
    await message.answer(f"Отлично, теперь напиши второе число:", reply_markup=math_buttons)
    await state.set_state(States.second_number)

@mydispatcher.message(States.second_number)
async def command_start(message: Message, state: FSMContext) -> None:
    await message.answer(f"Результат сложения ваших чисел: ", reply_markup=math_buttons)


@mydispatcher.message(F.text=="Минус")
async def command_start(message: Message) -> None:
    await message.answer(f"Тест кнопки МИНУС", reply_markup=math_buttons)
    



@mydispatcher.message(F.text=="Умножить")
async def command_start(message: Message) -> None:
    await message.answer(f"Тест кнопки Умножить", reply_markup=math_buttons)
   



@mydispatcher.message(F.text=="Главное меню")
async def command_start(message: Message) -> None:
    await message.answer(f"Главное меню", reply_markup=main_buttons)
    



@mydispatcher.message(F.text=="Текст")
async def command_start(message: Message) -> None:
    await message.answer(f"Тут должен быть текст", reply_markup=russian_buttons)
    




# По команде “/start” должна появляться клавиатура
# Скопировать Математика 
#   Текст По нажатию кнопки «Математика» должна появляться клавиатура
# Скопировать Плюс Минус Умножить 
#    Главное меню - По кнопкам «Плюс» «Минус» и «Умножить» должны быть соответствующие функции
# (на каждую кнопку выводить соотв текст "Тест кнопки ПЛЮС", "Тест кнопки МИНУС", "Тест кнопки УМНОЖИТЬ")
# - По нажатию «Главное меню» должна вновь появляться начальная клавиатура
# - По нажатию кнопки "Текст" должно высвечиваться сообщение "Тут должен быть текст". Клавиатура должна заменяться на:
# Скопировать Главное меню






if __name__ == "__main__":
    asyncio.run(main())