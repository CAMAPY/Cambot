import schedule
import time
import discord
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
from math import *
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
    schedule.every().day.at("17:15").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


def setup(client):
    client.add_cog(wish(client))