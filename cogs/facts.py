import discord
import sys
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
import random
import aiohttp

class facts(commands.Cog, description = "Get amazing facts"):
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
    @commands.command(help = "Get a random fact",brief = "Random fact on the go")
    async def fact(self,ctx):
        colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]
        fact = random.choice(open("facts.txt","r").readlines())
        fax = discord.Embed(title="Random fact", description=f'{fact}', color = random.choice(colors))
        await ctx.send(embed = fax)
    @commands.command(help = "Get a random disturbing fact",brief = "Random disturbing fact on the go",aliases = ["dfact"])
    async def disturbingfact(self,ctx):
        colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]
        fact = random.choice(open("dfacts.txt","r").readlines())
        fax = discord.Embed(title="Random Disturbing fact", description=f'{fact}', color = random.choice(colors))
        await ctx.send(embed = fax)
def setup(client):
    client.add_cog(facts(client))