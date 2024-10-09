from loader import dp, TIMECODE_1
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import asyncio
import time
import aiotable


@dp.message_handler(state=State.begin_waiting)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != texts.begin_btn:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.begin_kb)
        return
    
    await state.update_data(start=int(time.time()))
    await message.answer(texts.task_1_1)
    await message.answer(texts.task_1_2)
    await message.answer(texts.task_1_3, reply_markup=kb.flag_achieved_kb)

    await State.task_1_running.set()
    await asyncio.sleep(TIMECODE_1)
    data = await state.get_data()
    time_1 = data.get('time_1')
    if int(time_1) == 1:
        with open('images/running_fox.jpg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.timecode_1_1)
        await message.answer(texts.timecode_1_2, reply_markup=kb.flag_achieved_kb)
        

@dp.message_handler(state=State.task_1_running)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != texts.flag_achieved_btn:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.flag_achieved_kb)
        return
    await state.update_data(time_1=0)
    await message.answer(texts.task_question_1)
    await State.task_1_solving.set()


@dp.message_handler(state=State.task_1_solving)
async def send_welcome(message: types.Message, state: FSMContext):
    ans = ['гарри поттер', 'гари потер', 'гарри потер', 'гари поттер', 'harry potter']
    if message.text.lower() in ans:
        await message.answer(texts.r_letter)
        with open('images/r.jpg', 'rb') as photo:
            await message.answer_photo(photo)
        with open('images/fox_2.jpg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.task_1_correct)
        await message.answer(texts.task_1_correct_2, reply_markup=kb.run_next_kb)
        await State.task_1_solved.set()

        data = await state.get_data()
        start = data.get('start')
        finish = int(time.time())
        time_spent = texts.build_time(start, finish)
        try_count = data.get('try_count')
        id = str(message.from_id) + '-' + str(try_count) + 'new'
        await aiotable.update_cell(id, 6, time_spent.split('я: ')[1])
    else:
        await message.answer(texts.wrong_answer)




    
