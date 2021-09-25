import discord
import sys
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
import random
from math import *
import os


class ping(commands.Cog):

    def __init__(self,client): 
        self.client = client    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'`ping` reply has been turned on {self.client.user}')

    @commands.Cog.listener()
    async def on_message(self, message): 
        if self.client.user.mentioned_in(message):
                await message.channel.send("Hello there, I'm a bot send to learn your ways. My prefix is `;`. Use `;help` if you wanna know more. Get my only fans here: `prawnhub.com/phish`")
def setup(client):
    client.add_cog(ping(client))             
              