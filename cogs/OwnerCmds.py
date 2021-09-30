import discord
from discord.ext import commands, tasks
import os
from discord.ext.commands.converter import MemberConverter
from pretty_help import PrettyHelp,DefaultMenu
import json
import asyncio
import datetime,time
from discord.ext import cli
import asyncio

import discord
from discord import *
from discord.ext import commands
from discord.ext.commands.converter import MemberConverter
from discord.utils import get
from discord.user import *

import urllib.parse
import urllib.request
import re
import requests
import random
import json
import aiohttp

from math import floor


client = discord.Client

class OwnerCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("OwnerCommands Is Ready")

    @commands.command()
    @commands.is_owner()
    async def servers(self, ctx):
        servers = self.client.guilds
        for guild in servers:
            await ctx.send(guild)
    

    
    @commands.command(hidden = True)
    @commands.is_owner()
    async def rename(name):
        await client.user.edit(username=name)

    @commands.command(aliases = ["s"],hidden =True)
    @commands.is_owner()
    async def status(self, ctx, *, status=''):            #im the 
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game(status))
        await ctx.send(f'launching {status}.')

    @commands.command(aliases = ["quit", "q"],hidden = True)
    @commands.is_owner()
    async def close(self, ctx):
        await ctx.send(f"Ok bye! :wave:")
        await self.client.close()
        print("Ok bye! :wave:")

    @commands.command(hidden = True)
    @commands.is_owner()
    async def talk(self,ctx,*, arg):
        await ctx.send("lol")
        channel = client.get_channel(872371310704066633)
        await channel.send(f"{arg}")

def setup(client):
    client.add_cog(OwnerCommands(client))