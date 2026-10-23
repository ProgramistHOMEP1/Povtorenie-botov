import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message



mytoken = "8866695598:AAE51lbv-xCDGd8lw2suJosHvk0pIrCcI-4"
mybot = Bot(token=mytoken) 
mydispatcher = Dispatcher()


async def main():
    await mydispatcher.start_polling(mybot)


@mydispatcher.message(F.text=="/start")
async def command_start(message: Message) -> None:
    await message.answer("Привет, ")
    print(message.from_user)




if __name__ == "__main__":
    asyncio.run(main())