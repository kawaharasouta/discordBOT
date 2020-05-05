import discord
from discord.ext import tasks
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

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

@client.event
async def on_ready():
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
        print(name)
        print(times)
        m = "Hello " + message.author.name + "!"
        channel = client.get_channel(channel_id)
        #wks.update_acell('A1', 'Hello World!')
        await channel.send(m)
        #await message.channel.send(m)

@tasks.loop(seconds=1)
async def loop():
    m = "Hello " + "!"
    channel = client.get_channel(channel_id)
    await channel.send(m)

def main():
    client.run(key)

if __name__ == '__main__':
    main()
