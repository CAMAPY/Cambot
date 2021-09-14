import discord
import sys
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
import random
import aiohttp

class facts(commands.Cog):
    def __init__(self,client): 
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'facts has been turned on {self.client.user}')

    @commands.command(aliases = ["cf"], brief = "Get a cat fact", help = "catfact to make your day better")
    async def catfact(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://catfact.ninja/fact") as response:
                fact = (await response.json())["fact"]
                length = (await response.json())["length"]
                embed = discord.Embed(title=f'Random Cat Fact Number: **{length}**', description=f'Cat Fact: {fact}', colour=0x400080)
                embed.set_footer(text="")
                await ctx.send(embed=embed)
                await session.close()
    @commands.command()
    async def fact(self,ctx):
        fact = random.choice(open("facts.txt","r").readlines())
        fax = discord.Embed(title="Random fact", description=f'{fact}')
        await ctx.send(embed = fax)

def setup(client):
    client.add_cog(facts(client))