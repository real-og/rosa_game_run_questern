from loader import dp, TIMECODE_4, TIMECODE_4_2, TIMECODE_5
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import asyncio
import aiotable
import time


@dp.message_handler(state=State.task_3_solved)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != texts.run_next_btn:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.run_next_kb)
        return
    await message.answer(texts.task_4_1)
    await message.answer(texts.task_4_2, reply_markup=kb.flag_achieved_kb)
    await State.task_4_running.set()

    await asyncio.sleep(TIMECODE_4)
    data = await state.get_data()
    time_4 = data.get('time_4')
    if int(time_4) == 1:
        with open('images/running_fox_2.jpg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.timecode_4_1, reply_markup=kb.flag_achieved_kb)
        
    await asyncio.sleep(TIMECODE_4_2)
    data = await state.get_data()
    time_4_2 = data.get('time_4_2')
    if int(time_4_2) == 1:
        with open('images/win.jpg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.timecode_4_2)
        await message.answer(texts.timecode_4_3, reply_markup=kb.flag_achieved_kb)


@dp.message_handler(state=State.task_4_running)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != texts.flag_achieved_btn:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.flag_achieved_kb)
        return
    await state.update_data(time_4=0)
    await state.update_data(time_4_2=0)
    await message.answer(texts.task_question_4)
    await State.task_4_solving.set()


@dp.message_handler(state=State.task_4_solving)
async def send_welcome(message: types.Message, state: FSMContext):
    ans = ['венера']
    if message.text.lower() in ans:
        await message.answer(texts.a_letter)
        with open('images/a.jpg', 'rb') as photo:
            await message.answer_photo(photo)
        await message.answer(texts.task_question_4_2)
        await State.task_4_solved.set()

        data = await state.get_data()
        start = data.get('start')
        finish = int(time.time())
        time_spent = texts.build_time(start, finish)
        try_count = data.get('try_count')
        id = str(message.from_id) + '-' + str(try_count) + 'new'
        await aiotable.update_cell(id, 9, time_spent.split('я: ')[1])
    else:
        await message.answer(texts.wrong_answer)


@dp.message_handler(state=State.task_4_solved)
async def send_welcome(message: types.Message, state: FSMContext):
    ans = ['rosa']
    if message.text.lower() == 'роза':
        await message.answer(texts.change_to_latin)
        return
    if message.text.lower() in ans:
        await message.answer(texts.task_4_correct, reply_markup=kb.run_to_finish_kb)
        await State.task_4_solved_full.set()

        data = await state.get_data()
        start = data.get('start')
        finish = int(time.time())
        time_spent = texts.build_time(start, finish)
        try_count = data.get('try_count')
        id = str(message.from_id) + '-' + str(try_count) + 'new'
        await aiotable.update_cell(id, 10, time_spent.split('я: ')[1])
    else:
        await message.answer(texts.wrong_answer)


@dp.message_handler(state=State.task_4_solved_full)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != texts.run_to_finish_btn:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.run_to_finish_kb)
        return
    await message.answer(texts.task_5_1, reply_markup=kb.finished_kb)
    await State.running_finish.set()

    await asyncio.sleep(TIMECODE_5)
    data = await state.get_data()
    time_5 = data.get('time_5')
    if int(time_5) == 1:
        with open('images/tired.jpg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.timecode_5_1, reply_markup=kb.finished_kb)

