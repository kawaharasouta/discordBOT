import discord
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
client = discord.Client()
key = os.environ['DISCORD_KEY_VIDEO_MANAGEMENT']
#ebi_time = datetime.now() + relativedelta(hours=9)
#sango_time = ebi_time
#msg_desc = "さんご:" + sango_time.strftime('%Y/%m/%d %H:%M:%S')	 + "\n竹篭:" + ebi_time.strftime('%Y/%m/%d %H:%M:%S')	
url_list = []
list_num = 0
list_index = 0
msg_desc = "msg"
#msg = discord.Embed(title='養殖場 次回採取時間', description=msg_desc, colour=0x3498db)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print("discord key")
    print(key)
    print('------')
    global list_num
    text_data = open("url_list.txt", "r")
    lines = text_data.readlines()
    for line in lines:
        list_num = list_num + 1
        url_list.append(line)
    text_data.close()

@client.event
async def on_message(message):
    if message.content.startswith("!video"):
        if client.user != message.author:
            msg = await client.send_message(message.channel, url_list[0])
            #msg_rec = await client.send_message(message.channel, embed=msg)
            await client.add_reaction(msg, u"\U000025C0")
            await client.add_reaction(msg, u"\U000025B6")
#            await client.edit_message(msg, '編集0')
            client.loop.create_task(check_reaction(msg))

@client.event
async def check_reaction(target_msg):
    while True:
        target_reaction = await client.wait_for_reaction(message=target_msg)
        global list_num
        global list_index
        if target_reaction.user != target_msg.author:
            print(list_num)
            print(list_index)
            if target_reaction.reaction.emoji == u"\U000025C0":
                if list_index > 0:
                    print('次へ')
                    list_index = list_index - 1
                    await client.edit_message(target_msg, url_list[list_index])
                print('編集1')
            
            elif target_reaction.reaction.emoji == u"\U000025B6":
                if list_index < list_num - 2:
                    print('前へ')
                    list_index = list_index + 1
                    await client.edit_message(target_msg, url_list[list_index])
                print('編集2')
            
            else:
                pass
            
            await client.remove_reaction(target_msg, target_reaction.reaction.emoji, target_reaction.user)



def main():
    client.run(key)

if __name__ == '__main__':
    main()
