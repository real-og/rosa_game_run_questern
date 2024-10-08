from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
import logging
import os


logging.basicConfig(level=logging.WARNING)
ADMIN_ID = str(os.environ.get('ADMIN_ID'))
BOT_TOKEN = str(os.environ.get('BOT_TOKEN'))
FEEDBACK_GROUP_ID = str(os.environ.get('FEEDBACK_GROUP_ID'))

TIMECODE_1 = 3
TIMECODE_2 = 3
TIMECODE_2_2 = 3
TIMECODE_3 = 3
TIMECODE_3_2 = 3
TIMECODE_4 = 3
TIMECODE_4_2 = 3
TIMECODE_5 = 3

# storage = RedisStorage2(db=2)
storage = MemoryStorage()

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)