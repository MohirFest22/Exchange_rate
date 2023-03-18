import logging
import requests

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = ' '

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Where USD is the base currency you want to use
url_usd = 'https://v6.exchangerate-api.com/v6/a1adfd4fbb31605d813e708c/pair/USD/UZS'
url_rub = 'https://v6.exchangerate-api.com/v6/a1adfd4fbb31605d813e708c/pair/RUB/UZS'

# Making our request

response1,response2 = requests.get(url_usd), requests.get(url_rub)
data1,data2 = response1.json(), response2.json()

# Your JSON object

@dp.message_handler(commands=['start', 'boshlash'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum!\n Valyutalar kursi botiga xush kelibiz!\nMenulardan birini tanlang:")
    await message.answer(" /usd_uzs -- AQSH dollar kursi\n/rub_uzs -- Rossiya rubl kursi")

@dp.message_handler(commands=['usd_uzs'])
async def money(message: types.Message):
	javob_usd = f"{data1['time_next_update_utc']} vaqti bilan!\n1 {data1['base_code']} dollar: {data1['conversion_rate']} {data1['target_code']}"
	await message.reply(javob_usd)

@dp.message_handler(commands=['rub_uzs'])
async def money(message: types.Message):
	javob_rub = f"{data2['time_next_update_utc']} vaqti bilan!\n1 {data2['base_code']} rubl: {data2['conversion_rate']} {data2['target_code']}"
	await message.reply(javob_rub)

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)