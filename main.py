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

if avatar_id == 10000002:
	avatar_pic = ayaka
if avatar_id == 10000003:
	avatar_pic = jean
if avatar_id == 10000005:
	avatar_pic = aether
if avatar_id == 10000006:
	avatar_pic = lisa
if avatar_id == 10000007:
	avatar_pic = lumine
if avatar_id == 10000014:
	avatar_pic = barbara
if avatar_id == 10000015:
	avatar_pic = kaeya
if avatar_id == 10000016:
	avatar_pic = diluc
if avatar_id == 10000020:
	avatar_pic = razor
if avatar_id == 10000021:
	avatar_pic = amber
if avatar_id == 10000022:
	avatar_pic = venti
if avatar_id == 10000023:
	avatar_pic = xiangling
if avatar_id == 10000024:
	avatar_pic = beidou
if avatar_id == 10000025:
	avatar_pic = xingqui
if avatar_id == 10000026:
	avatar_pic = xiao
if avatar_id == 10000027:
	avatar_pic = ningguang
if avatar_id == 10000029:
	avatar_pic = klee
if avatar_id == 10000030:
	avatar_pic = zhongli
if avatar_id == 10000031:
	avatar_pic = fischl
if avatar_id == 10000032:
	avatar_pic = bennett
if avatar_id == 10000033:
	avatar_pic = tartaglia
if avatar_id == 10000034:
	avatar_pic = noel
if avatar_id == 10000035:
	avatar_pic = qiqi
if avatar_id == 10000036:
	avatar_pic = chongyun
if avatar_id == 10000037:
	avatar_pic = ganyu
if avatar_id == 10000038:
	avatar_pic = albedo
if avatar_id == 10000039:
	avatar_pic = diona
if avatar_id == 10000041:
	avatar_pic = mona
if avatar_id == 10000042:
	avatar_pic = keqing
if avatar_id == 10000043:
	avatar_pic = sucrose
if avatar_id == 10000044:
	avatar_pic = xinyan
if avatar_id == 10000045:
	avatar_pic = rosaria
if avatar_id == 10000046:
	avatar_pic = hutao
if avatar_id == 10000047:
	avatar_pic = kazuha
if avatar_id == 10000048:
	avatar_pic = yanfei
if avatar_id == 10000049:
	avatar_pic = yoimiya
if avatar_id == 10000050:
	avatar_pic = thoma
if avatar_id == 10000051:
	avatar_pic = eula
if avatar_id == 10000052:
	avatar_pic = raiden_shogun
if avatar_id == 10000053:
	avatar_pic = sayu
if avatar_id == 10000054:
	avatar_pic = kokomi
if avatar_id == 10000055:
	avatar_pic = gorou
if avatar_id == 10000056:
	avatar_pic = sara
if avatar_id == 10000057:
	avatar_pic = itto
if avatar_id == 10000058:
	avatar_pic = yae_miko
if avatar_id == 10000059:
	avatar_pic = heizo
if avatar_id == 10000060:
	avatar_pic = yelan
if avatar_id == 10000062:
	avatar_pic = aloy
if avatar_id == 10000063:
	avatar_pic = shenhe
if avatar_id == 10000064:
	avatar_pic = yunjin
if avatar_id == 10000065:
	avatar_pic = shinobu
if avatar_id == 10000066:
	avatar_pic = ayato
if avatar_id == 10000067:
	avatar_pic = collie
if avatar_id == 10000068:
	avatar_pic = dori
if avatar_id == 10000069:
	avatar_pic = tighnari
if avatar_id == 10000070:
	avatar_pic = nilou
if avatar_id == 10000071:
	avatar_pic = cyno
if avatar_id == 10000072:
	avatar_pic = candace




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
        user_nickname = (f"Nickname: {user.player.nickname}")
        user_level = (f"Adventure Rank: {user.player.level}")
        user_worldlevel = (f'World level:{user.player.worldLevel}')
        user_abyss = (f'Abyss: {user.player.towerFloorIndex}-{user.player.towerLevelIndex}')
        avatar_id = (f"Avtar id: {user.player.profilePicture.avatarId}")
        await event.reply("{}\nUID : {}\n{}\n{}\n{}\n{}\n\nIs this your id??".format(user_nickname, list_of_words[1], user_level, user_worldlevel, avatar_id, user_abyss)
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
