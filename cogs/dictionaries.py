import discord
import sys
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
import random


class Rps(commands.Cog, help = "Rps commands"):

    def __init__(self,client): 
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'`rps` has been turned on {self.client.user}')



    @commands.command(help = "Play rock-paper-scissors with me!", brief= "Lose at rock-paper-scissors with me")
    async def rps(self, ctx):
        rpsGame = ['rock', 'paper', 'scissors']
        players = set()
        if ctx.author.id in players:
            return
        players.add(ctx.author.id)
        await ctx.send(f"Rock, paper, or scissors? Get ready to lose.")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame
        
        user_choice = (await self.client.wait_for('message', check=check)).content

        comp_choice = random.choice(rpsGame)
        if user_choice == 'rock':
            if comp_choice == 'rock':
                await ctx.send(f'Huh, we tied.\nYour choice: `{user_choice}`\nMy choice: `{comp_choice}`')
            elif comp_choice == 'paper':
                await ctx.send(f'Noob I win.\nYour choice: `{user_choice}`\nMy choice: `{comp_choice}`')
            elif comp_choice == 'scissors':
                await ctx.send(f"*gasps* You won? This isn't possible, I'm rebooting....\nYour choice: `{user_choice}`\nMy choice: `{comp_choice}`")

        elif user_choice == 'paper':
            if comp_choice == 'rock':
                await ctx.send(f'Noob i win.\nYour choice: `{user_choice}`\nMy choice: `{comp_choice}`')
            elif comp_choice == 'paper':
                await ctx.send(f'huh, we tied.\nYour choice: `{user_choice}`\nMy choice: `{comp_choice}`')
            elif comp_choice == 'scissors':
                await ctx.send(f"*gasps* This isn't possible, I'm rebooting....\nYour choice: `{user_choice}`\nMy choice: `{comp_choice}`")

        elif user_choice == 'scissors':
            if comp_choice == 'rock':
                await ctx.send(f'Noob i win.\nYour choice: `{user_choice}`\nMy choice: `{comp_choice}`')
            elif comp_choice == 'paper':
                await ctx.send(f"*gasps* This isn't possible, i'm rebooting....\nYour choice: `{user_choice}`\nMy choice: `{comp_choice}`")
            elif comp_choice == 'scissors':
                await ctx.send(f"Huh, we tied.\nYour choice: `{user_choice}`\nMy choice: `{comp_choice}`")
        players.discard(ctx.author.id)

def setup(client):
    client.add_cog(Rps(client))
