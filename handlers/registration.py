from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable


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
    await message.answer(texts.ask_number, reply_markup=kb.number_kb)
    await State.waiting_for_number.set()
    await state.update_data(name=name) 


@dp.message_handler(state=State.waiting_for_number, content_types=['any'])
async def send_welcome(message: types.Message, state: FSMContext):
    if (not message.contact) and (message.text != texts.no_btn):
        await message.answer(texts.wrong_btn_input, reply_markup=kb.number_kb)
        return

    phone_number = 'Не указал'
    if message.contact:
        phone_number = message.contact.phone_number

    
    await message.answer(texts.rules)
    await message.answer(texts.rules_2)
    await message.answer(texts.rules_3, reply_markup=kb.begin_kb)
    await State.begin_waiting.set()

    data = await state.get_data()
    try_count = data.get('try_count')
    name = data.get('name')
    id = str(message.from_id) + '-' + str(try_count) + 'new'
    await aiotable.append_user(id, str(message.from_user.username), str(phone_number), str(name))
    


