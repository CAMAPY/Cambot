import discord
import sys
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
import random
from math import *
import os
from discord.ext.commands.converter import MemberConverter
 

class moderation(commands.Cog, description = "Moderators moderating around"):

    def __init__(self,client): 
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'moderation has been turned on {self.client.user}')

    @commands.command(brief = 'Kicks members', help = 'Kicks members')
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, user: discord.Member, *, reason="No reason provided"):
            await user.kick(reason=reason)
            kick = discord.Embed(title=f"get outta here {user.name}", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
            await ctx.message.delete()
            await ctx.channel.send(embed=kick)
            await user.send(embed=kick)
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(self, error, commands.MissingPermissions):
            error = discord.Embed(title=f"I can't do that, {ctx.name}", description=f"You don't have admin.")
            await ctx.send("You don't the permissions to do that buddy. :pensive:")

    @commands.command(brief ="Bans members", help  ="Bans members")
    @commands.has_permissions(administrator=True)
    async def ban(self,ctx, member : discord.Member, *, reason = None):
        await member.ban(reason = reason)
        await ctx.send(f'Banned {member.mention}')
    
    @commands.command(pass_context=True, brief = "Deletes multiple messages", help = 'Delete multiple messages (needs admin permissions)')
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, limit: int):
            await ctx.channel.purge(limit=limit)
            await ctx.send('Messages cleared by {}'.format(ctx.author.mention))
            await ctx.message.delete()

    @commands.command(pass_context=True, brief="Changes nick of people", help = "Changes nick of people")
    @commands.has_permissions(manage_nicknames=True)
    async def nick(self, ctx, member: MemberConverter, nick):
        await member.edit(nick=nick)
        await ctx.send(f'Nickname was changed for `@{member.name}` ')

def setup(client):
    client.add_cog(moderation(client))