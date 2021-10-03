import discord
import sys
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
import random
from math import *
import os


class delete(commands.Cog, description = "-ud -a is cringe", name = "-ud -a killer"):

    def __init__(self,client): 
        self.client = client
    @commands.Cog.listener()
    async def on_message(self, message): 
        if message.author == self.client.user:
            return 
        if "up to 10 last deleted messages (last hour or 12 hours for premium):" in message.content.lower():
            await message.delete()
    