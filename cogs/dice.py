import discord
import sys
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
import random
from math import *
import os
from discord.ext.commands.converter import MemberConverter

class dice(commands.Cog):

    def __init__(self,client): 
        self.client = client

    @commands.command(brief = "dice roll", help = "roll a dice to get a number between 1 and 6")
    async def roll(self,ctx): 
        numbers = random.randint(1, 6)
        await ctx.channel.send(f"{numbers}, {ctx.author.name}")

    @commands.command(aliases = ["droll"], brief = "Two dice rolls at once!!" , help = "Two dice rolls at once!!")
    async def doubleroll(self, ctx): 
        numbers = random.randint(1, 6)
        number = random.randint(1, 6)
        await ctx.channel.send(f"{numbers}; {number}, {ctx.author.name}")
def setup(client):
    client.add_cog(dice(client))