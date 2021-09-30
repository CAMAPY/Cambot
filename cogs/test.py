import discord
import sys
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
import random
from math import *
import os
from discord.ext.commands.converter import MemberConverter
 

class testing(commands.Cog):

    def __init__(self,client): 
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Test has been turned on {self.client.user}')


    @commands.command(aliases=["t"],brief="Literally just replies with whats in your message after the command")
    async def test(self,ctx,*, arg):
        await ctx.message.delete()
        await ctx.send(arg)
        channel = self.client.get_channel(872371310704066633)
        await channel.send(f"{arg}, requested by {ctx.author.name}")
def setup(client):
    client.add_cog(testing(client))