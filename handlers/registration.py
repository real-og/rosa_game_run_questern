from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State


@dp.message_handler(state=State.starting)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.choose_enemy_btn:
        with open('images/start_fox.jpg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.fox_greeting)
        await State.entering_name.set()
    else:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.choose_enemy_kb)


@dp.message_handler(state=State.entering_name)
async def send_welcome(message: types.Message, state: FSMContext):
    name = message.text
    await message.answer(texts.rules)
    await message.answer(texts.rules_2)
    await message.answer(texts.rules_3, reply_markup=kb.begin_kb)
    await State.begin_waiting.set()
    await state.update_data(name=name) 
