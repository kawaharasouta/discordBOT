import discord
from discord.ext import tasks
import os
import gspread
import datetime

class Onetime_Member:
    time = 0
    num_member = 0
    member = []
    def __init__(self, time):
        self.time = time
    def show_onetime_member(self):
        ret = str(self.time) + '\t' + 'member:\t'
        for i in range(len(self.member)):
            ret = ret + self.member[i] + '\t'
        return ret

class Day_Member:
    times = []
    def __init__(self):
        for i in range(20, 25):
            self.times.append(Onetime_Member(i))
    def Show_Day_Member(self):
        ret = str(datetime.date.today()) + '\n'
        #print(len(self.times))
        for i in range(len(self.times)):
            #print(self.times[i].show_onetime_member())
            ret += self.times[i].show_onetime_member() + '\n'
        print(ret)


async def one_raised_hand(sheet, name, times, channel):
    print(name)
    print(times)
    m = "Hello " + name + "!"
    await channel.send(m)



