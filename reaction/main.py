import discord
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
client = discord.Client()
key = os.environ['DISCORD_KEY']
ebi_time = datetime.now() + relativedelta(hours=9)
sango_time = ebi_time
msg_desc = "さんご:" + sango_time.strftime('%Y/%m/%d %H:%M:%S')	 + "\n竹篭:" + ebi_time.strftime('%Y/%m/%d %H:%M:%S')	
msg = discord.Embed(title='養殖場 次回採取時間', description=msg_desc, colour=0x3498db)

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
	if message.content.startswith("switch"):
		if client.user != message.author:
			#msg = await client.send_message(message.channel, 'スイッチ')
			msg_rec = await client.send_message(message.channel, embed=msg)
			await client.add_reaction(msg_rec, u"\U0001F48E")
			await client.add_reaction(msg_rec, u"\U0001F990")
			client.loop.create_task(check_reaction(msg_rec))

@client.event
async def check_reaction(target_msg):
	"""
	指定のメッセージにリアクションがついたらメッセージを送る
	"""
	while True:
		target_reaction = await client.wait_for_reaction(message=target_msg)
		if target_reaction.user != target_msg.author:
			global ebi_time
			global sango_time
			if target_reaction.reaction.emoji == u"\U0001F990":
				ebi_time = datetime.now() + relativedelta(hours=5)
				msg_desc = "さんご:" + sango_time.strftime('%Y/%m/%d %H:%M:%S')	 + "\n竹篭:" + ebi_time.strftime('%Y/%m/%d %H:%M:%S')	
				await client.send_message(target_msg.channel, "エビ")
				client.edit_message(msg, msg_desc) ##
			
			elif target_reaction.reaction.emoji == u"\U0001F48E":
				sango_time = datetime.now() + relativedelta(hours=10)
				msg_desc = "さんご:" + sango_time.strftime('%Y/%m/%d %H:%M:%S')	 + "\n竹篭:" + ebi_time.strftime('%Y/%m/%d %H:%M:%S')	
				await client.send_message(target_msg.channel, "さんご")
				client.edit_message(msg, msg_desc) ##
			
			else:
				pass
			
			await client.remove_reaction(target_msg, target_reaction.reaction.emoji, target_reaction.user)



def main():
	client.run(key)

if __name__ == '__main__':
	main()
