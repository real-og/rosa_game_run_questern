from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
from loader import FEEDBACK_GROUP_ID
import time
import aiotable


@dp.message_handler(state=State.running_finish)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != texts.finished_btn:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.finished_kb)
        return
    await state.update_data(time_5=0)
    await message.answer(texts.end_1)
    await message.answer(texts.ask_secret)
    await State.secret_submitting.set()


@dp.message_handler(state=State.secret_submitting)
async def send_welcome(message: types.Message, state: FSMContext):
    ans = ['скорость']
    if message.text.lower() in ans:
        data = await state.get_data()
        start = data.get('start')
        finish = int(time.time())
        time_spent = texts.build_time(start, finish)
        await message.answer(time_spent)
        await message.answer(texts.end_2)
        await message.answer(texts.gift_getting, reply_markup=kb.gift_kb)
        await State.waiting_for_gift.set()

        try_count = data.get('try_count')
        id = str(message.from_id) + '-' + str(try_count)
        await aiotable.update_cell(id, 4, time_spent.split('я: ')[1])
    else:
        await message.answer(texts.wrong_answer)


@dp.message_handler(state=State.waiting_for_gift)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != texts.gift_btn:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.gift_kb)
        return
    with open('images/rosa.jpg', 'rb') as photo:
        await message.answer_photo(photo, caption=texts.end_3)
    with open('images/fox_wave.jpg', 'rb') as photo:
        await message.answer_photo(photo, caption=texts.end_4)
    await message.answer(texts.end_5)
    await State.feedback_submitting.set()


@dp.message_handler(state=State.feedback_submitting, content_types=['any'])
async def send_welcome(message: types.Message, state: FSMContext):
    try:
        await bot.forward_message(FEEDBACK_GROUP_ID, message.chat.id, message.message_id)
    except:
        await bot.send_message(FEEDBACK_GROUP_ID, f'Ошибка пересылки от {message.from_id}')
    with open('images/bot_wave.jpg', 'rb') as photo:
        await message.answer_photo(photo, caption=texts.end_6)
    await State.end.set()
    
