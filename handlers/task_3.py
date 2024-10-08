from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State


@dp.message_handler(state=State.task_2_solved)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != texts.run_next_btn:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.run_next_kb)
        return
    await message.answer(texts.task_3_1)
    await message.answer(texts.task_3_2, reply_markup=kb.flag_achieved_kb)
    await State.task_3_running.set()


@dp.message_handler(state=State.task_3_running)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != texts.flag_achieved_btn:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.flag_achieved_kb)
        return
    await message.answer(texts.task_question_3)
    await State.task_3_solving.set()


@dp.message_handler(state=State.task_3_solving)
async def send_welcome(message: types.Message, state: FSMContext):
    ans = ['греция', 'древняя греция', 'греции', 'в греции', 'древней греции', 'в древней греции']
    if message.text.lower() in ans:
        with open('images/o.jpg', 'rb') as photo:
            await message.answer_photo(photo)
        with open('images/fox_2.jpg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.task_3_correct)
        await message.answer(texts.task_3_correct_2, reply_markup=kb.run_next_kb)
        await State.task_3_solved.set()
    else:
        await message.answer(texts.wrong_answer)
