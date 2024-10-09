from loader import BOT_TOKEN
from aiogram import Bot
import asyncio


text = "Текст рассылки"


with open('ids.txt', 'r') as f:
    ids = f.read().split()

for i in range(len(ids)):
    ids[i] = int(ids[i].split('-')[0]) 


async def broadcast(ids, text, token):
    bot = Bot(token=token, parse_mode="HTML")
    s = await bot.get_session()
    for id in ids:
        try:
            await bot.send_message(id, text=text)
            print(str(id) + ' - ok')
        except:
            me = await bot.get_me()
            print(f"{id} нет в боте {me.username} - {me.first_name}")
    await s.close()


if __name__ == "__main__":
    asyncio.run(broadcast(ids, text, BOT_TOKEN))

