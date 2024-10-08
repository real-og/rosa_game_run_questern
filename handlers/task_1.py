from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State


@dp.message_handler(state=State.begin_waiting)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != texts.begin_btn:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.begin_kb)
        return
    
    await message.answer(texts.task_1_1)
    await message.answer(texts.task_1_2)
    await message.answer(texts.task_1_3, reply_markup=kb.flag_achieved_kb)

    await State.task_1_running.set()


@dp.message_handler(state=State.task_1_running)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != texts.flag_achieved_btn:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.flag_achieved_kb)
        return
    
    await message.answer(texts.task_question_1)
    await State.task_1_solving.set()


@dp.message_handler(state=State.task_1_solving)
async def send_welcome(message: types.Message, state: FSMContext):
    ans = ['гарри поттер', 'гари потер', 'гарри потер', 'гари поттер', 'harry potter']
    if message.text.lower() in ans:
        with open('images/r.jpg', 'rb') as photo:
            await message.answer_photo(photo)
        with open('images/fox_2.jpg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.task_1_correct)
        await message.answer(texts.task_1_correct_2, reply_markup=kb.run_next_kb)
        await State.task_1_solved.set()
    else:
        await message.answer(texts.task_question_1_wrong)




    
