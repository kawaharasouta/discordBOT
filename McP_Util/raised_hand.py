import discord
from discord.ext import tasks
import os
import gspread

class Onetime_Member:
    time = 0
    num_member = 0
    member = []
    def __init__(self, time):
        self.time = time

class Day_Member:
    times = []
    def __init__(self):
        for i in range(20, 24):
            self.times.append(Onetime_Member(i))





async def one_raised_hand(sheet, name, times, channel):
    print(name)
    print(times)
    m = "Hello " + name + "!"
    await channel.send(m)



