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
    async def on_ready(self):
        print(f'webhooks has been turned on {self.client.user}')
    async def get_cambot_webhook(self, channel: discord.TextChannel) -> discord.Webhook:
        webhooks = await channel.webhooks()
        cambot_hook = next((i for i in webhooks if i.name == "cambot"), None)
        if not cambot_hook:
            cambot_hook = await channel.create_webhook(name="cambot")
        return cambot_hook
    @commands.Cog.listener()
    async def on_message(self, message):
        if "canopy" in message.content.lower():
            await message.delete()
            content = message.content.replace("canopy", "camapy")

            cambot_hook = await self.get_cambot_webhook(message.channel)
            if cambot_hook is None:
                cambot_hook = await message.channel.create_webhook(name = "cambot")
            webhook_message = await cambot_hook.send(
                content=content,
                username=message.author.display_name,
                avatar_url=message.author.avatar_url,
                wait=True,
            )
    @commands.Cog.listener()
    async def on_message(self, message):
        if "asdasda" in message.content.lower():
            await message.delete()
            content = message.content.replace("basdasdawrwersfvu", "befaesdjuhgdfbtsruh")
            cambot_hook = await self.get_cambot_webhook(message.channel)
            if cambot_hook is None:
                cambot_hook = await message.channel.create_webhook(name = "cambot")
            webhook_message = await cambot_hook.send(
                content=content,
                username=message.author.display_name,
                avatar_url=message.author.avatar_url,
                wait=True,
            )
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):  
            error = str(error).split(":")[-1]
            error = discord.Embed(title=f"❌Error encountered❌", description=f"{error}", colour = 0x660000) 
            await ctx.send(embed = error)
    @commands.command(aliases = [')'], hidden = True)
    async def wink():
        pass
def setup(client):
    client.add_cog(ew(client))  