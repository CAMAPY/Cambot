import discord
import sys
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
import random
from math import *
import os
from discord.ext.commands.converter import MemberConverter
 

class TechSupport(commands.Cog):

    def __init__(self,client): 
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Tech Support has been turned on {self.client.user}')
     
    @commands.command()
    async def techsupport(self, ctx):
        devices = ['Automated Dildo', 'Vibrator', 'Automatic Pet Feeder', "PlayStation 2", "Smart Watch"]
        await ctx.send(f"Good day Sir/Madam, Thank you for calling tech-support regarding your {random.choice(devices)}")
    