import discord
import sys
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
import random
from math import *
import os


class game(commands.Cog, description = "game?!"):

    def __init__(self,client): 
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'game has been turned on {self.client.user}')
        
    @commands.command()
    async def wordle(self, ctx,difficulty):
        async def gameplay():
                statement = (await self.client.wait_for('message', check = check)).content
                if statement != word:
                    for j in range(len(statement)):
                        if statement[j] in word:
                            if statement[j] in word[j]:
                                statement[j] = '🟩'
                            else:
                                statement[j] = '🟨'
                    await ctx.send(statement)
                else:
                    await ctx.send("YOU GOT IT!! ggwp")
        def check(message):
            return message.channel == ctx.channel and len(message.content) ==  x
        await ctx.send("Get ready to rack your brains for epic wordle game!")
        wordseasy = ['abs', 'add', 'bag', 'bad', 'cap', 'can', 'cam', 'cad', 'dad', 'dal', 'ear', 'eat', 'eco', 'fam', 'far', 'fan', 'gag', 'had', 'ham', 'ice','icy', 'jar', 'jam']
        wordshard = ['abacus', 'baboon', 'babies', 'babble', 'cabbed', 'canned', 'cabbie', 'dabber', 'eager', 'eagles', 'fabled', 'fabric','facade','fables', 'gabble', 'habits', 'hacked', 'hacker'
        'kebabs', 'machos', 'pacify', 'pacing', 'pacers', 'packed', 'rabbit', 'tables', 'tabbed', 'tablas', 'udders','vaccum', 'vacant', 'vacate', 'wackos', 'yachts', 'zaatar']
        wordsmed = []
        if (difficulty.lower() == 'easy') or (difficulty.lower() == 'e'):
            x = 3
            word = random.choice(wordseasy)
            for i in range(2):
                await gameplay()

        elif (difficulty.lower() == 'medium') or (difficulty.lower() == 'm'):
            x = 5
            word = random.choice(wordsmed)
        elif (difficulty.lower() == 'hard') or (difficulty.lower() == 'h'):
            x = 6
            word = random.choice(wordshard)
            for i in range(6):
                await gameplay()



def setup(client):
    client.add_cog(game(client))