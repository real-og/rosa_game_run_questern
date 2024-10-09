from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
import logging
import os


logging.basicConfig(level=logging.WARNING)

BOT_TOKEN = str(os.environ.get('BOT_TOKEN'))
FEEDBACK_GROUP_ID = str(os.environ.get('FEEDBACK_GROUP_ID'))
SHEET_LINK = str(os.environ.get('SHEET_LINK'))

TIMECODE_1 = 5 * 60
TIMECODE_2 = 2 * 60
TIMECODE_2_2 = 5 * 60
TIMECODE_3 = 1 * 60
TIMECODE_3_2 = 4 * 60
TIMECODE_4 = 2 * 60
TIMECODE_4_2 = 5 * 60
TIMECODE_5 = 3 * 60

# storage = RedisStorage2(db=2)
storage = MemoryStorage()

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)