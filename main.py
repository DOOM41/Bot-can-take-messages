from aiogram import Bot, Dispatcher, types, executor

from conf import BOT_API
from utils import set_bot_code

bot = Bot(token=BOT_API)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands='start')
async def start_mess(message: types.Message):
    await message.answer(
        "Здавствуй я бот который может принимать сообщения с другого сервиса\n\
Для отправки сообщении пропиши команду /set_code {code} и отправь код который видишь на главной транице сайта"
    )
    
@dp.message_handler(commands='set_code')
async def set_code(message: types.Message):
    code = message.get_args().replace(" ","")
    if not code:
        await message.answer("Введите код!")
        return
    res = await set_bot_code(code, message.chat.id)
    if res:
        await message.answer("Код сохранен!")
        return
    await message.answer("Вы уже вводили код")


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)