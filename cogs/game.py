import discord
import sys
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
import random
from math import *
import os


class game(commands.Cog, description = "game?!"):

    def __init__(self,client): 
        self.client = client
    @commands.command
    async def game(self, ctx):
        msg = await ctx.send("React to this message to join the epic game")
        await self.client.add_reaction(msg, "✔")





def setup(client):
    client.add_cog(game(client))