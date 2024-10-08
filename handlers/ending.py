from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
from loader import FEEDBACK_GROUP_ID


@dp.message_handler(state=State.running_finish)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != texts.finished_btn:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.finished_kb)
        return
    await message.answer(texts.ask_secret)
    await State.secret_submitting.set()


@dp.message_handler(state=State.secret_submitting)
async def send_welcome(message: types.Message, state: FSMContext):
    ans = ['скорость']
    if message.text.lower() in ans:
        await message.answer(texts.end_1)
        with open('images/fox_wave.jpg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.end_2)
        await message.answer(texts.end_3)
        await message.answer(texts.end_4)
        await message.answer(texts.end_5)
        with open('images/bot_wave.jpg', 'rb') as photo:
            await message.answer_photo(photo)
        
        await State.feedback_submitting.set()
    else:
        await message.answer(texts.wrong_answer)



@dp.message_handler(state=State.feedback_submitting, content_types=['any'])
async def send_welcome(message: types.Message, state: FSMContext):
    try:
        await bot.forward_message(FEEDBACK_GROUP_ID, message.chat.id, message.message_id)
    except:
        await bot.send_message(FEEDBACK_GROUP_ID, f'Ошибка пересылки от {message.from_id}')
        
            







