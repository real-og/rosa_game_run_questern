from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import time
import asyncio


@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    with open('images/start.jpg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.greeting)
    await message.answer(texts.greeting_2, reply_markup=kb.choose_enemy_kb)
    await State.starting.set()
    await state.update_data(time_1=1)
    await state.update_data(time_2=1)
    await state.update_data(time_2_2=1)
    await state.update_data(time_3=1)
    await state.update_data(time_3_2=1)
    await state.update_data(time_4=1)
    await state.update_data(time_4_2=1)
    await state.update_data(time_5=1)
    


