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
import pymongo


API_ID = os.environ.get('API_ID', None)
API_HASH = os.environ.get('API_HASH', None)
TOKEN = os.environ.get('TOKEN', None)
api_id = API_ID
api_hash = API_HASH
bot_token = TOKEN
url = "mongodb+srv://telegramgenshindatabase:telegramgenshindatabase@genshinbot.kne6n9m.mongodb.net/?retryWrites=true&w=majority"
db_name = "genshinbot"
collection_name = "userdata"
cluster = Mongoclient(url)

client = TelegramClient('aucbout', api_id, api_hash).start(bot_token=bot_token) #i dont really understand it lol but without this bot wont work

genshinclient = Enka()

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', #copy pasted from telethon docs lol..... so usually it logs error

                    level=logging.WARNING)





if __name__ == '__main__':
    try:
        print("Initializing Database...")
        # Connect to local database
        db = cluster[db_name]
        data = db[collection_name]
        client.run_until_disconnected()

    except Exception as error:
        print('Cause: {}'.format(error))
