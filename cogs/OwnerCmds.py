import discord
from discord.ext import commands
import os
import asyncio

import discord
from discord import *
from discord.ext import commands
from discord.ext.commands.converter import MemberConverter
from discord.user import *



client = discord.Client

class OwnerCommands(commands.Cog, description = "Commands for daddy :weary:"):

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
    async def rename(self, name):
        await self.client.user.edit(username=name)

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
        channel = self.client.get_channel(874866927938449471)
        await channel.send(f"{arg}")
    
    @commands.command(name="toggle", description="Enable or disable a command!")
    @commands.is_owner()
    async def toggle(self, ctx, *, command):
        command = self.client.get_command(command)

        if command is None:
            embed = discord.Embed(title="ERROR", description="I can't find a command with that name!", color=0xff0000)
            await ctx.send(embed=embed)

        elif ctx.command == command:
            embed = discord.Embed(title="ERROR", description="You cannot disable this command.", color=0xff0000)
            await ctx.send(embed=embed)

        else:
            command.enabled = not command.enabled
            ternary = "enabled" if command.enabled else "disabled"
            embed = discord.Embed(title="Toggle", description=f"I have {ternary} {command.qualified_name} for you!", color=0xff00c8)
            await ctx.send(embed=embed)


    @commands.command(hidden = True)
    @commands.is_owner()
    async def message(self, member : discord.Member, *, message):
        await member.send(message)
def setup(client):
    client.add_cog(OwnerCommands(client))