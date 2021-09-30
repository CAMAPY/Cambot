import discord
from discord.ext import commands

client = discord.Client

class OwnerCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("OwnerCommands Is Ready")

    @commands.command()
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
    async def say(ctx, *,arg):
        channel = client.get_channel(873983296269348884)
        await channel.send(arg)

def setup(client):
    client.add_cog(OwnerCommands(client))