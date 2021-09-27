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
            colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]
            reply = discord.Embed(title="Hello :wave:", description=f"I'm a bot send to learn your ways. My prefix is `;`. Use `;help` if you wanna know more \nGet my only-fans here: [CambotHelp.com](https://www.youtube.com/watch?v=dQw4w9WgXcQ)]', color = random.choice(colors)") 
            await message.channel.send(reply)
def setup(client):
    client.add_cog(ping(client))             
              