
import time
import discord
import sys
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
import random
from math import *
import os
from discord.ext.commands.converter import MemberConverter
from discord.ext import tasks

client = discord.Client 

class wish(commands.Cog):

    def __init__(self,client): 
        self.client = client
    @commands.Cog.listener()
    async def job():
        channel = client.get_channel(874866927938449471)
        await channel.send("Happy New Day!")
    # Run job every day at specific HH:MM and next HH:MM:SS
    schedule.every().day.at("22:30").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


def setup(client):
    client.add_cog(wish(client))