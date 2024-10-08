from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State


@dp.message_handler(state=State.task_3_solved)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != texts.run_next_btn:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.run_next_kb)
        return
    await message.answer(texts.task_4_1)
    await message.answer(texts.task_4_2, reply_markup=kb.flag_achieved_kb)
    await State.task_4_running.set()


@dp.message_handler(state=State.task_4_running)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != texts.flag_achieved_btn:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.flag_achieved_kb)
        return
    await message.answer(texts.task_question_4)
    await State.task_4_solving.set()


@dp.message_handler(state=State.task_4_solving)
async def send_welcome(message: types.Message, state: FSMContext):
    ans = ['венера']
    if message.text.lower() in ans:
        with open('images/a.jpg', 'rb') as photo:
            await message.answer_photo(photo)
        await message.answer(texts.task_question_4_2)
        await State.task_4_solved.set()
    else:
        await message.answer(texts.wrong_answer)


@dp.message_handler(state=State.task_4_solved)
async def send_welcome(message: types.Message, state: FSMContext):
    ans = ['rosa']
    if message.text.lower() in ans:
        with open('images/rosa.jpg', 'rb') as photo:
            await message.answer_photo(photo)
        await message.answer(texts.task_4_correct, reply_markup=kb.run_to_finish_kb)
        await State.task_4_solved_full.set()
    else:
        await message.answer(texts.wrong_answer)


@dp.message_handler(state=State.task_4_solved_full)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != texts.run_to_finish_btn:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.run_to_finish_kb)
        return
    await message.answer(texts.task_5_1, reply_markup=kb.finished_kb)
    await State.running_finish.set()

