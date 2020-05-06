import discord
from discord.ext import tasks
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import raised_hand as hand

# discord info
client = discord.Client()
key = os.environ['DISCORD_KEY']
channel_id = 540544808360345612

# gspread info
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('mcp-util.json', scope)
gc = gspread.authorize(credentials)
wkb = gc.open('McP_Util Test')
wks = wkb.sheet1
raised_hand_sheet = wkb.worksheet('raised_hand')

Member = hand.Day_Member()
channel = None

async def usage():
    m = '''
        ***McP Util usage***
        now under developed.
    '''
    await channel.send(m)
    


@client.event
async def on_ready():
    global channel
    channel = client.get_channel(channel_id)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print("discord key")
    print(key)
    print('------')
    #loop.start()


@client.event
async def on_message(message):
    if message.content.startswith("/can"):
        name = message.author.display_name
        times = message.content.split()
        times.pop(0)
        m = hand.one_raise_hand(Member, name, times)
        if m != None:
            await channel.send(m)
        await channel.send(Member.Show_Day_Member())
        ##wks.update_acell('A1', 'Hello World!')
    elif message.content.startswith("/not"):
        name = message.author.display_name
        times = message.content.split()
        times.pop(0)
        m = hand.one_lower_hand(Member, name, times)
        if m != None:
            await channel.send(m)
        await channel.send(Member.Show_Day_Member())
    elif message.content.startswith("/show"):
        await channel.send(Member.Show_Day_Member())
    elif message.content.startswith("/utilhelp"):
        await usage()
        

@tasks.loop(seconds=1)
async def loop():
    m = "Hello " + "!"
    await channel.send(m)

def main():
    client.run(key)

if __name__ == '__main__':
    main()
