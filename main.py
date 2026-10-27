import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from dotenv import load_dotenv
import os


load_dotenv()
mytoken = os.getenv("TOKEN")

mybot = Bot(token=mytoken) 
mydispatcher = Dispatcher()

async def main():
    await mydispatcher.start_polling(mybot)


@mydispatcher.message(F.text=="/start")
async def command_start(message: Message) -> None:
    await message.answer(f"Привет, {message.from_user.first_name}")
    print(message.from_user)


@mydispatcher.message(F.text=="/donat")
async def command_start(message: Message) -> None:
    await message.answer(f"{message.from_user.first_name}, Вы хотите сделать донат?\n Реквизиты для доната: +5674986587 Ульфа-Банк")
    print(message.from_user)

@mydispatcher.message(F.text.startswith("/better "))
async def command_age(message):
    print(message.text)
    newtext = message.text.split(" ")
    if int(newtext[1])>int(newtext[2]):
        await message.answer(f"Число {newtext[1]} больше!")
    if int(newtext[2])>int(newtext[1]):
        await message.answer(f"Число {newtext[2]} больше!")
    if int(newtext[1])==int(newtext[2]):
        await message.answer(f"Число ваши числа одинаковые!")

# Домашнее задание:
# Создать бота с тремя командами: 
# /start - выводить приветствие
# /donat - выводить информацию о том, куда тебе можно донатить
# /better N1 N2 - выводить большее из двух чисел (N1 - первое число, N2 - второе число)




if __name__ == "__main__":
    asyncio.run(main())