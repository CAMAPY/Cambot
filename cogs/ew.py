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
            webhooks = await message.channel.webhooks()
            webhook = await message.channel.create_webhook(name = message.author.name)
def setup(client):
    client.add_cog(ew(client))