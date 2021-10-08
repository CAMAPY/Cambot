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
    async def get_cambot_webhook(self, channel: discord.TextChannel) -> discord.Webhook:
        webhooks = await channel.webhooks()
        cambot_hook = next((i for i in webhooks if i.name == "cambot"), None)
        if not cambot_hook:
            cambot_hook = await channel.create_webhook(name="cambot")
        return cambot_hook
    @commands.Cog.listener()
    async def on_message(self, message): 
        if "ew" in message.content.lower():
            content = f"OMG that sounds awesome!!"
            await message.delete()
            cambot_hook = await self.get_cambot_webhook(message.channel)
            if cambot_hook is None:
                cambot_hook = await message.channel.create_webhook(name = "cambot")
            webhook_message = await cambot_hook.send(
                content=content,
                username=message.author.display_name,
                avatar_url=message.author.avatar_url,
                wait=True,
            )

        if "canopy" in message.content.lower():
            content = message.content.replace("canopy", "camapy")
            await message.delete()
            cambot_hook = await self.get_cambot_webhook(message.channel)
            if cambot_hook is None:
                cambot_hook = await message.channel.create_webhook(name = "cambot")
            webhook_message = await cambot_hook.send(
                content=content,
                username=message.author.display_name,
                avatar_url=message.author.avatar_url,
                wait=True,
            )

def setup(client):
    client.add_cog(ew(client))  