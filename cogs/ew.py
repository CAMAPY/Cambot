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
    async def on_message(self, message): 
        target_content = self.targets.get(message.author.id)
        if target_content and "ew" in message.content.lower() in message.content.lower():
            content = "OMG that sounds awesome!"
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