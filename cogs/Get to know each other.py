import discord
import sys
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
import random
from math import *
import os


class Fun(commands.Cog):

    def __init__(self,client): 
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'stalk has been turned on {self.client.user}')

    @commands.command(aliases=["ts"],brief="Literally just replies with whats in your message after the command")
    async def truthsuggest(self,ctx,*, arg):
        channel = self.client.get_channel(883983603921453086)
        await ctx.send(f"`{arg}` has been suggested, please wait for it to be verified")
        await channel.send(f"{arg}, requested by {ctx.author.name}")
    @commands.command()
    async def truth(self, ctx):
        truth = ['When was the last time you masturbated?', 'If you were a porn-star, would you masturbate to yourself?', 'Tell us one of your pet-peeves', 'What\'s the most embarassing thing you\'ve done?', 
        "What's something about you that you're parents don't know?", "What celebrity would you like to have dinner with? (not exactly as a date)", "What's something that you would erase in the past?", "What's an app that you don't like but still use?", 
        "What's your biggest fear?" ,"Do you have any fetishes?", "Do you currently have a crush on anyone?", "What's your biggest turn-on?", "Who was your first celebrity crush?", "What's your biggest insecurity?", "What's the best thing anyone's ever done for you?"
        , "What's the worst thing anyone's ever done to you?", "What's your worst habit?", "How many times a day do you masturbate?", "What's the perfect meal for you?", "Would you call your friends trustworthy?", "Do you have a best friend?", "What's your unpopular opinon?", "Who here do u think is the most desperate?",
        "What do you think is your most under-rated talent?", "What are you most self conscious about?", "Who do you look up to the most?", "What fictional character do you most relate to?", "What's the worst thing about the opposite gender?", "Who is your crush?", "Do you prefer 3D women or 2D women?", "What's the worst cliche in anime?",
        ""]
        await ctx.send(f"{random.choice(truth)}")

    @commands.command(aliases = ["ng"])
    async def numbergame(self,ctx):
        num = random.randint(1,146)
        if num in range(1,45):
            await ctx.send('https://media.discordapp.net/attachments/862667294428889129/886633593957417000/unknown.png?width=1253&height=701')
        elif num in range(45, 100):
            await ctx.send("https://media.discordapp.net/attachments/862667294428889129/886633647560597584/unknown.png?width=1249&height=701"
        elif num in range(100, 134):
            await ctx.send("https://media.discordapp.net/attachments/862667294428889129/886633720432443432/unknown.png?width=1246&height=701")

def setup(client):
    client.add_cog(Fun(client))