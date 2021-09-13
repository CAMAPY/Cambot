import discord
import sys
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
import random
from math import *
import os
from discord.ext.commands.converter import MemberConverter
 

class moderation(commands.Cog):

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
        if isinstance(error, commands.MissingPermissions):
            error = discord.Embed(title=f"I can't do that, {ctx.name}", description=f"You don't have admin.")
            await ctx.send("You don't the permissions to do that buddy. :pensive:")

    @commands.command(brief ="Bans members", help  ="Bans members")
    @commands.has_permissions(administrator=True)
    async def ban(self,ctx, member : discord.Member, *, reason = None):
        await member.ban(reason = reason)
        await ctx.send(f'Banned {member.mention}')
    
    @commands.command(pass_context=True, brief = "deletes multiple messages", help = 'Delete multiple messages (needs admin permissions)')
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, limit: int):
            await ctx.channel.purge(limit=limit)
            await ctx.send('Messages cleared by {}'.format(ctx.author.mention))
            await ctx.message.delete()


    @commands.command(pass_context=True, brief="Changes nick of people")
    @commands.has_permissions(administrator=True)
    async def nick(self, ctx, member: MemberConverter, nick):
        await member.edit(nick=nick)
        await ctx.send(f'Nickname was changed for `@{member.name}` ')

    @commands.Cog.listener()
    async def on_message(self, message): 
        if "what the fuck did you just fucking say about me, you little bitch?" in message.content.lower():
            await message.channel.send(f"stop. posting. this. it isn't funny, {message.author.mention}")
            await message.delete()
    @commands.Cog.listener()
    async def on_message(self, message):  
        if "fap" in message.content.lower():
            if message.author.id == 275609153274380289:
                await message.channel.send("Bruh, koshy don't fap again")
    @commands.Cog.listener()
    async def on_message(self, message):  
        if "ironic" in message.content:
            if message.author.id == 680298420338294796:
                await message.channel.send("learn to use ironic properly dumbfuck")
    @commands.Cog.listener()
    async def on_message(self, message):  
        if "iwabii" in message.content:
            await message.channel.send("Ibrahims at it again lmao")
    @commands.Cog.listener()
    async def on_message(self, message): 
        possible_responses = [ 'hello', 'suppers', 'yo wassup', 'stfu dumbass', 'what do u want this time?', 'ok now what?', 'hello daddy :drooling_face:' ] 
        if "cambot" in message.content.lower():
            await message.channel.send(f"{random.choice(possible_responses)} {message.author.mention}")
    @commands.Cog.listener()
    async def on_message(self, message):  
        if "^" in message.content:
            if message.author.id == 398429963990335489:
                await message.channel.send("your mom's exponential weight gain be like")


def setup(client):
    client.add_cog(moderation(client))