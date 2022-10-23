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
import genshinstats as gs
from enkapy import Enka
import sqlite3



API_ID = os.environ.get('API_ID', None)
API_HASH = os.environ.get('API_HASH', None)
TOKEN = os.environ.get('TOKEN', None)
api_id = API_ID
api_hash = API_HASH
bot_token = TOKEN

client = TelegramClient('aucbout', api_id, api_hash).start(bot_token=bot_token) #i dont really understand it lol but without this bot wont work

genshinclient = Enka()

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', #copy pasted from telethon docs lol..... so usually it logs error

                    level=logging.WARNING)

test_image = 'https://telegra.ph/file/a71d3d2cfd43aee7bf388.jpg'

firstcharacter = 'https://telegra.ph/file/3239fa6a6b0ad4da03b78.jpg'

secondcharacter = 'https://telegra.ph/file/c54a2d5a67f6c96ceada0.jpg'

thirdcharacter = 'https://telegra.ph/file/df286deeed0cc82f481b9.jpg'

fourthcharacter = 'https://telegra.ph/file/f405812782f8748e7d636.jpg'

fifthcharacter = 'https://telegra.ph/file/e1c18bda34dba94e9d17e.jpg'

sixthcharacter = 'https://telegra.ph/file/c2224b650b098df5b7870.jpg'

seventhcharacter = 'https://telegra.ph/file/2ffd3f840c50aafff9229.jpg'

eighthcharacter = 'https://telegra.ph/file/5e033bdb03c3dd319547c.jpg'


@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    sender = await event.get_sender()
    await client.send_message(event.sender_id, 'Me alive what about u')
    await genshinclient.load_lang()
    user = await genshinclient.fetch_user(849166888)
    print(f"Nickname: {user.player.nickname}")
    print(f"Level: {user.player.level}")
    print(f'Signature: {user.player.signature}')
    print(f'World level:{user.player.worldLevel}')
    print(f'Abyss: {user.player.towerFloorIndex}-{user.player.towerLevelIndex}')
    # fetch first character
    character = user.characters[1]
    print(f'Name: {character.name}')
    print(f'Ascension: {character.ascension}')
    print(f'Level: {character.level}')
    print(f'Exp: {character.experience}')
    print('Weapon:')
    weapon = character.weapon
    print(f'\tName: {weapon.name}')
    print(f'\tLevel: {weapon.level}')
    print(f'\tRefine: {weapon.refine}')
    print(f'\tStar level: {weapon.rank}')

    print('Constellations:')
    for constellation in character.constellations:
        if constellation.activated:
            print(f'\t{constellation.name} Activated')
    print('Skills:')
    for skill in character.skills:
        if skill.type == 0:
            print(f'\tNormal skill {skill.name}, level:{skill.level}')
        elif skill.type == 1:
            print(f'\tElemental skill {skill.name}, level:{skill.level}')
        elif skill.type == 2:
            print(f'\tElemental burst {skill.name}, level:{skill.level}')
    print('Artifacts:')
    for artifact in character.artifacts:
        print(f'\t{artifact.set_name} {artifact.name}:')
        print(f'\t{artifact.main_stat.prop}:{artifact.main_stat.value}')
        for sub_stats in artifact.sub_stats:
            print(f'\t\t{sub_stats.prop}:{sub_stats.value}')


@client.on(events.NewMessage(pattern='/login'))
async def handler(event):
    list_of_words = event.message.text.split(" ")
    user_id = event.sender_id
    genshinid = list_of_words[1]
    user = await genshinclient.fetch_user(genshinid)
    text = (f"Nickname: {user.player.nickname}")
    text += (f"Level: {user.player.level}")
    await event.reply("Logged in as "+str(genshinid))
    await event.reply(text)

@client.on(events.NewMessage(pattern='/mycharacter'))
async def handler(event):
    await client.send_file(event.chat_id, file = test_image, caption = 'select which character u want to see'
         ,
         buttons=[
                  [
                     Button.inline('1', 'first_character'),
                     Button.inline('2', 'second_character'),
                     Button.inline('3', 'third_character'),
                     Button.inline('4', 'fourth_character')
                  ],
                  [
                     Button.inline('5', 'fifth_character'),
                     Button.inline('6', 'sixth_character'),
                     Button.inline('7', 'seventh_character'),
                     Button.inline('8', 'eighth_character')
                  ]
                 ]
                )

@client.on(events.CallbackQuery(data='first_character'))
async def approvecb(event):
     await client.send_file(event.chat_id, firstcharacter)
     await client.delete_messages(event.chat_id, event.message_id)

@client.on(events.CallbackQuery(data='second_character'))
async def approvecb(event):
     await client.send_file(event.chat_id, secondcharacter)
     await client.delete_messages(event.chat_id, event.message_id)

@client.on(events.CallbackQuery(data='third_character'))
async def approvecb(event):
     await client.send_file(event.chat_id, thirdcharacter)
     await client.delete_messages(event.chat_id, event.message_id)

@client.on(events.CallbackQuery(data='fourth_character'))
async def approvecb(event):
     await client.send_file(event.chat_id, fourthcharacter)
     await client.delete_messages(event.chat_id, event.message_id)

@client.on(events.CallbackQuery(data='fifth_character'))
async def approvecb(event):
     await client.send_file(event.chat_id, fifthcharacter)
     await client.delete_messages(event.chat_id, event.message_id)

@client.on(events.CallbackQuery(data='sixth_character'))
async def approvecb(event):
     await client.send_file(event.chat_id, sixthcharacter)
     await client.delete_messages(event.chat_id, event.message_id)

@client.on(events.CallbackQuery(data='seventh_character'))
async def approvecb(event):
     await client.send_file(event.chat_id, seventhcharacter)
     await client.delete_messages(event.chat_id, event.message_id)

@client.on(events.CallbackQuery(data='eighth_character'))
async def approvecb(event):
     await client.send_file(event.chat_id, eighthcharacter)
     await client.delete_messages(event.chat_id, event.message_id)

@client.on(events.NewMessage(pattern='/build'))
async def start(event):
    chat = await event.get_chat()
    list_of_words = event.message.text.split(" ")
    character_name = list_of_words[1]
    pattern = r'(?i).*kazuha'
    if character_name in pattern:
        await client.send_message(event.chat_id,"huihui")



if __name__ == '__main__':
    try:
        print("Initializing Database...")
        # Connect to local database
        db_name = 'genshin.db' # Insert the database name. Database is the folder
        conn = sqlite3.connect(db_name, check_same_thread=False)
        # Create the cursor
        # The cursor is an instance using which you can invoke methods that execute SQLite statements, fetch data from the result sets of the queries.
        crsr = conn.cursor() 
        print("Connected to the database")

        # Command that creates the "oders" table 
        sqlgenshin_command = """CREATE TABLE IF NOT EXISTS Legendary( 
            user_id VARCHAR(200),
            genshin_id VARCHAR(200));"""
        crsr.execute(sqlgenshin_command)
        print("Legendary table is ready")

        print("Bot Started")
        client.run_until_disconnected()

    except Exception as error:
        print('Cause: {}'.format(error))
