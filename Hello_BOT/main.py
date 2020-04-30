import discord
import os
client = discord.Client()
key = os.environ['DISCORD_KEY']

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print("discord key")
    print(key)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("おはよう"):
        if client.user != message.author:
            m = "Hello " + message.author.name + "!"
            #await client.send_message(message.channel, m)
            await message.channel.send(m)

def main():
    client.run(key)

if __name__ == '__main__':
    main()
