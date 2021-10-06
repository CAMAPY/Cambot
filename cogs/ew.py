import discord
import sys
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
import random
from math import *
import os


class ew(commands.Cog, description = "ew is cringe"):

    def __init__(self,client): 
        self.client = client
    @commands.Cog.listener()
    async def on_message(self, message): 
        if "ew" in message.content.lower():
            await message.author.ban()
            await message.channel.send(f'Banned {message.author.name}')
def setup(client):
    client.add_cog(ew(client))