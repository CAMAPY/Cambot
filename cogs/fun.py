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
        "How does your dream boy or girl look like?", "Who is the last person you texted for?", "Do you think you will get married to your current girlfriend/boyfriend?", "How many selfies do you take in a day?", "What is something that no one else knows about you?", "Who do you hate the most?","Would you change genders? Why?",
         "Would you let your best friend cheat on a test?","Is there anything about your life you would want to change?","Do you talk in your sleep?","Are you scared of the dark?", "Do you write in a diary?", "If you could marry a celebrity, who would it be?", "If you want to change a few things about your body, what would those be?", "You have to give up one makeup item for the rest of your life. What is it?", "Do you ever talk to yourself in the mirror?", "What would be in your web history that you do not want anybody to see?", "If you have suddenly become invisible, what would you do?", "What was the strangest dream you ever had?", "How many times have you gone out without a shower?", 
        "How long have you gone without brushing your teeth?", "If you could be reincarnated into anyone’s body, who would you want to become?", "Did you ever share your close friend’s secret with others?", "Have you ever cried during a movie? If so, which one?", "Would you share a toothbrush with your best friend?", "Who’s the most boring person here and in your life?", "What was your most embarrassing moment in public?", "What is the worst habit that you are happy to do?", "What's something that is unhealthy for you, but you still do it?", "How do you impress your boyfriend /girlfriend/crush?", "Of the people in this server, who would you go out with?", "Who is the funniest person here?", "What's the dumbest thing you've ever done on a dare?"
        ,"If you were stuck on a deserted island which friend would you want with you?", "What was your childhood nickname (and why)?", "Have you ever cheated on a test?", "Are you scared of dying? Why?", "What do you think is your biggest physical flaw?", "If you could invent anything, what would it be?", "What does your sibling know about you that no one else does?", "If you could be a superhero, what would your power be?", "Given the choice, would you want to hang out with your parents?", "Would you rather eat a pigeon or a subway rat?", "Would you do anything for money?", "What personality traits would cause you to end a friendship?", "Have you ever told a lie during a game of Truth? What was it and why?", "Which person here knows something about you that you wouldn't want revealed?", "Have you ever pretended to be older or younger than you are to be able to do something?", ""]
        await ctx.send(f"{random.choice(truth)}")

    @commands.command(help = "Get to know your friends with the number game!", brief= "number game vibes",aliases = ["ng"])
    async def numbergame(self,ctx):
        num = random.randint(1,134) 
        if num in range(1,45):
            await ctx.send('https://media.discordapp.net/attachments/862667294428889129/886633593957417000/unknown.png?width=1253&height=701')
        elif num in range(45, 100):
            await ctx.send("https://media.discordapp.net/attachments/862667294428889129/886633647560597584/unknown.png?width=1249&height=701")
        elif num in range(100, 134):
            await ctx.send("https://media.discordapp.net/attachments/862667294428889129/886633720432443432/unknown.png?width=1246&height=701")
        await ctx.send(f"And you have to answer question number: {num}")

def setup(client):
    client.add_cog(Fun(client))