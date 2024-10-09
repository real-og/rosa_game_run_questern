from loader import dp, TIMECODE_3, TIMECODE_3_2
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import asyncio


@dp.message_handler(state=State.task_2_solved)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != texts.run_next_btn:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.run_next_kb)
        return
    await message.answer(texts.task_3_1)
    await message.answer(texts.task_3_2, reply_markup=kb.flag_achieved_kb)
    await State.task_3_running.set()

    await asyncio.sleep(TIMECODE_3)
    data = await state.get_data()
    time_3 = data.get('time_3')
    if int(time_3) == 1:
        await message.answer(texts.timecode_3_1, reply_markup=kb.flag_achieved_kb)
        
    await asyncio.sleep(TIMECODE_3_2)
    data = await state.get_data()
    time_3_2 = data.get('time_3_2')
    if int(time_3_2) == 1:
        with open('images/win.jpg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.timecode_3_2)
        await message.answer(texts.timecode_3_3, reply_markup=kb.flag_achieved_kb)


@dp.message_handler(state=State.task_3_running)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != texts.flag_achieved_btn:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.flag_achieved_kb)
        return
    await state.update_data(time_3=0)
    await state.update_data(time_3_2=0)
    await message.answer(texts.task_question_3)
    await State.task_3_solving.set()


@dp.message_handler(state=State.task_3_solving)
async def send_welcome(message: types.Message, state: FSMContext):
    ans = ['греция', 'древняя греция', 'греции', 'в греции', 'древней греции', 'в древней греции']
    if message.text.lower() in ans:
        await message.answer(texts.o_letter)
        with open('images/o.jpg', 'rb') as photo:
            await message.answer_photo(photo)
        with open('images/fox_2.jpg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.task_3_correct)
        await message.answer(texts.task_3_correct_2, reply_markup=kb.run_next_kb)
        await State.task_3_solved.set()
    else:
        await message.answer(texts.wrong_answer)
