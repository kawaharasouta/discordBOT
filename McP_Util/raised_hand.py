import discord
from discord.ext import tasks
import os
import gspread
import datetime

class Onetime_Member:
    def __init__(self, time):
        self.time = time
        self.num_member = 0
        self.member = []
    def show_onetime_member(self):
        ret = str(self.time) + '\t' + 'member:\t'
        for i in range(self.num_member):
            ret = ret + self.member[i] + '\t'
        return ret
    def is_already_member(self, name):
        for i in range(self.num_member):
            if name == self.member[i]:
                return True
        return False
    def add_member(self, name):
        self.num_member += 1
        self.member.append(name)
    def del_member(self, name):
        self.num_member -= 1
        self.member.remove(name)

class Day_Member:
    def __init__(self):
        self.times = []
        for i in range(20, 25):
            self.times.append(Onetime_Member(i))
    def Show_Day_Member(self):
        ret = str(datetime.date.today()) + '\n'
        for i in range(len(self.times)):
            ret += str(self.times[i].num_member) + '\t' + self.times[i].show_onetime_member() + '\n'
        return ret
    def Add_Member(self, name, time):
        for i in range(len(self.times)):
            if self.times[i].time == int(time):
                if not self.times[i].is_already_member(name):
                    self.times[i].add_member(name)
                return
        return str(time)
    def Del_Member(self, name, time):
        for i in range(len(self.times)):
            if self.times[i].time == int(time):
                if self.times[i].is_already_member(name):
                    self.times[i].del_member(name)
                return
        return str(time)

def one_raise_hand(member, name, times):
    ret = []
    for i in range(len(times)):
        r = member.Add_Member(name, times[i])
        if r != None:
           ret.append(r)
    if len(ret) == 1:
        m = ','.join(ret) + ' is not set.'
        return m
    elif len(ret) > 1:
        m = ','.join(ret) + ' are not set.'
        return m

def one_lower_hand(member, name, times):
    ret = []
    for i in range(len(times)):
        r = member.Del_Member(name, times[i])
        if r != None:
           ret.append(r)
    if len(ret) == 1:
        m = ','.join(ret) + ' is not set.'
        return m
    elif len(ret) > 1:
        m = ','.join(ret) + ' are not set.'
        return m

