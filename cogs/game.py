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
                win = False
                for i in range(int(difficulty)):
                    statement = (await self.client.wait_for('message', check = check)).content
                    answer = ''
                    print(word)
                    if win == False:
                        for j in range(len(statement)):
                            if statement[j] in word:
                                if statement[j] in word[j]:
                                    k = '🟩'
                                else:
                                    k = '🟨'
                            else:
                                k = '❌'
                            answer += k
                        await ctx.send(answer)
                        await ctx.send(f"You've {len(statement) - j} more tries")
                    else:
                        win = True
                        await ctx.send("Congrats you won! ggwp")
                        break
        async def cwin(win):
                if win == True:
                    await ctx.send("Congrats you won! ggwp")
                else:
                    await ctx.send("Oops, Your out of tries, try again")
        def check(message):
            return message.channel == ctx.channel and len(message.content) ==  int(difficulty)
        await ctx.send("Get ready to rack your brains for epic wordle game!")
        await ctx.send("Start guessing!")
        wordseasy = ['abs', 'add', 'bag', 'bad', 'cap', 'can', 'cam', 'cad', 'dad', 'dal', 'ear', 'eat', 'eco', 'fam', 'far', 'fan', 'gag', 'had', 'ham', 'ice','icy', 'jar', 'jam']
        wordshard = ['abacus', 'baboon', 'babies', 'babble', 'cabbed', 'canned', 'cabbie', 'dabber', 'eager', 'eagles', 'fabled', 'fabric','facade','fables', 'gabble', 'habits', 'hacked', 'hacker'
        'kebabs', 'machos', 'pacify', 'pacing', 'pacers', 'packed', 'rabbit', 'tables', 'tabbed', 'tablas', 'udders','vaccum', 'vacant', 'vacate', 'wackos', 'yachts', 'zaatar']
        win = False
        if difficulty == '3':
            word = random.choice(wordseasy)
            await ctx.send(f'Start guessing a {difficulty} lettered word')
            win = False 
            await gameplay()
            await cwin(win)
        elif difficulty == "6":
            word = random.choice(wordshard)
            await ctx.send(f'Start guessing a {difficulty} lettered word')
            await gameplay()
            await cwin(win)
        else:
            await ctx.send("That's not a valid length, Please choose either 6 or 3")


def setup(client):
    client.add_cog(game(client))