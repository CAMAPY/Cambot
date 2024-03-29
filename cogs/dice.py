import discord
import sys
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
import random
from math import *
import os
from discord.ext.commands.converter import MemberConverter

class dice(commands.Cog, description = "Get your life-choices done with these dices"):

    def __init__(self,client): 
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'stalk has been turned on {self.client.user}')
    @commands.command(brief = "dice roll", help = "roll a dice to get a number between 1 and 6")
    async def roll(self,ctx): 
        numbers = random.randint(1, 6)
        await ctx.channel.send(f"{numbers}, {ctx.author.name}")

    @commands.command(aliases = ["droll"], brief = "Two dice rolls at once!!" , help = "Two dice rolls at once!!")
    async def doubleroll(self, ctx): 
        numbers = random.randint(1, 6)
        number = random.randint(1, 6)
        await ctx.channel.send(f"{numbers}; {number}, {ctx.author.name}")
    @commands.command()
    async def choose(self, ctx, choices):
        a, b = choices.split(' ', 1)
        await ctx.send(f"{a}")
        await ctx.send(f"I choose `{random.choice(a,b)}`, By the power vested in me by MakeDumbassDecisions.com")
def setup(client):
    client.add_cog(dice(client))