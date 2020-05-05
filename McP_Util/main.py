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

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print("discord key")
    print(key)
    print('------')
    #loop.start()

async def f_one_raised_hand(fsheet, fname, ftimes, fchannel):
    print(fname)
    print(ftimes)
    m = "Hello " + fname + "!"
    await fchannel.send(m)

@client.event
async def on_message(message):
    if message.content.startswith("/can"):
        name = message.author.display_name
        times = message.content.split()
        times.pop(0)
        channel = client.get_channel(channel_id)
        await hand.one_raised_hand(raised_hand_sheet, name, times, channel)
        #print(name)
        #print(times)
        #m = "Hello " + message.author.name + "!"
        ##wks.update_acell('A1', 'Hello World!')
        #await channel.send(m)

@tasks.loop(seconds=1)
async def loop():
    m = "Hello " + "!"
    channel = client.get_channel(channel_id)
    await channel.send(m)

def main():
    client.run(key)

if __name__ == '__main__':
    main()
