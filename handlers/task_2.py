from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State


@dp.message_handler(state=State.task_1_solved)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != texts.run_next_btn:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.run_next_kb)
        return
    await message.answer(texts.task_2_1)
    await message.answer(texts.task_2_2, reply_markup=kb.flag_achieved_kb)
    await State.task_2_running.set()


@dp.message_handler(state=State.task_2_running)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != texts.flag_achieved_btn:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.flag_achieved_kb)
        return
    await message.answer(texts.task_question_2)
    await State.task_2_solving.set()


@dp.message_handler(state=State.task_2_solving)
async def send_welcome(message: types.Message, state: FSMContext):
    ans = ['часы']
    if message.text.lower() in ans:
        with open('images/s.jpg', 'rb') as photo:
            await message.answer_photo(photo)
        with open('images/fox_back.jpg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.task_2_correct)
        await message.answer(texts.task_2_correct_2, reply_markup=kb.run_next_kb)
        await State.task_2_solved.set()
    else:
        await message.answer(texts.wrong_answer)
