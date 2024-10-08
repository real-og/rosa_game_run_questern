from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import texts


choose_enemy_kb = ReplyKeyboardMarkup([[texts.choose_enemy_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

begin_kb = ReplyKeyboardMarkup([[texts.begin_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

flag_achieved_kb = ReplyKeyboardMarkup([[texts.flag_achieved_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

run_next_kb = ReplyKeyboardMarkup([[texts.run_next_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

run_to_finish_kb = ReplyKeyboardMarkup([[texts.run_to_finish_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

finished_kb = ReplyKeyboardMarkup([[texts.finished_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)


