import discord
import sys
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
import random
from math import *
import os


class aliveabot(commands.Cog):

    def __init__(self,client): 
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'I has been turned on {self.client.user}')

    @commands.Cog.listener()
    async def on_message(self, message): 
        possible_responses = [ 'hello', 'suppers', 'yo wassup', 'stfu dumbass', 'what do u want this time?', 'ok now what?', 'hello daddy :drooling_face:', "bruh", "my name is not to be invoked, he might be close..." ] 
        if "cambot" in message.content.lower():
            await message.channel.send(f"{random.choice(possible_responses)} {message.author.mention}")
        elif "^" in message.content and message.author.id == 398429963990335489:
                await message.channel.send("your mom's exponential weight gain be like")
                await message.delete()
        elif "iwabii" in message.content.lower():
            await message.channel.send("Ibrahims at it again lmao")
        elif "ironic" in message.content.lower() and message.author.id == 680298420338294796:
                await message.channel.send("learn to use ironic properly dumbfuck")
                await message.delete()
        elif "fap" in message.content.lower() and message.author.id == 275609153274380289:
                await message.channel.send("Bruh, koshy don't fap again")
        elif "what the fuck did you just fucking say about me, you little bitch?" in message.content.lower():
            await message.channel.send(f"stop. posting. this. it isn't funny, {message.author.mention}")
            await message.delete()
        elif "The storm that wipes out the pathetic little thing you call your life" in message.content.lower():
            await message.channel.send(f"nice try dumbass {message.author.mention}")
            await message.delete()
        elif message.content.startswith('^botservers'):
            await message.channel.send("I'm in " + str(len(self.client.guilds)) + " servers!")
def setup(client):
    client.add_cog(aliveabot(client))