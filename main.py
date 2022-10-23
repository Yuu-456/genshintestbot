import os
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from time import sleep
from telethon.tl.types import MessageEntityCode
from telethon import TelegramClient, events, Button
import telethon.sync #lol copied from docs
import asyncio
import logging
import asyncio
from telethon import events
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from enkapy import Enka
from pymongo import MongoClient


API_ID = os.environ.get('API_ID', None)
API_HASH = os.environ.get('API_HASH', None)
TOKEN = os.environ.get('TOKEN', None)
api_id = API_ID
api_hash = API_HASH
bot_token = TOKEN
url = "mongodb+srv://telegramgenshindatabase:telegramgenshindatabase@genshinbot.kne6n9m.mongodb.net/?retryWrites=true&w=majority"
db_name = "genshinbot"
collection_name = "userdata"
cluster = MongoClient(url)

client = TelegramClient('aucbout', api_id, api_hash).start(bot_token=bot_token) #i dont really understand it lol but without this bot wont work

genshinclient = Enka()

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', #copy pasted from telethon docs lol..... so usually it logs error

                    level=logging.WARNING)


@client.on(events.NewMessage(pattern="(?i)/insert"))
async def insert(event):
      # Get the sender of the message
      sender = await event.get_sender()
      SENDER = sender.id
      # Get the text of the user AFTER the /insert command and convert it to a list (we are splitting by the SPACE " " simbol)
      list_of_words = event.message.text.split(" ")
      name = list_of_words[1]
      post_dict = {"User_id" : SENDER, "GENSHIN_ID" : name}
      data.insert_one(post_dict)
      
@client.on(events.NewMessage(pattern="/login"))
async def insert(event):
      sender = await event.get_sender()
      SENDER = sender.id
      list_of_words = event.message.text.split(" ")
      if list_of_words[1].isnumeric():
        await genshinclient.load_lang()
        user = await genshinclient.fetch_user(list_of_words[1])
        print(user)
        user_nickname = (f"Nickname: {user.player.nickname}")
        user_level = (f"Adventure Rank: {user.player.level}")
        user_worldlevel = (f'World level:{user.player.worldLevel}')
        user_abyss = (f'Abyss: {user.player.towerFloorIndex}-{user.player.towerLevelIndex}')
        await event.reply("{}\nUID : {}\n{}\n{}\n{}\n\nIs this your id??".format(user_nickname, list_of_words[1], user_level, user_worldlevel, user_abyss)
            ,
            buttons=[
            [
                Button.inline('Yes', 'yes'),
                Button.inline('No', 'no')
            ]
        ]
       )


if __name__ == '__main__':
    try:
        print("Initializing Database...")
        # Connect to local database
        db = cluster[db_name]
        data = db[collection_name]
        print("bot started")
        client.run_until_disconnected()

    except Exception as error:
        print('Cause: {}'.format(error))
