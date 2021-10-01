import discord
import sys
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
import random
from math import *
import os


class aliveabot(commands.Cog):

    def __init__(self,client): 
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'I has been turned on {self.client.user}')

    @commands.Cog.listener()
    async def on_message(self, message): 
        possible_responses = [ 'hello', 'suppers', 'yo wassup', 'stfu dumbass', 'what do u want this time?', 'ok now what?', 'hello daddy :drooling_face:', "bruh", "my name is not to be invoked, he might be close..." ]
        if message.author == self.client.user:
            return 
        elif "cambot" in message.content.lower():
            await message.channel.send(f"{random.choice(possible_responses)} {message.author.mention}")
        elif "^" in message.content and message.author.id == 398429963990335489:
                await message.channel.send("your mom's exponential weight gain be like")
                await message.delete()
        elif "im dad" in message.content.lower():
            if message.author.id == 756391739056586773:
                name = "joel"
            elif message.author.id == 738980178314657822:
                name = "aditya"
            elif message.author.id == 553871925177221120:
                name = "akhil"
            else:
                name = "bro"
            await message.channel.send(f"Nice innovative joke, {name}")
        elif "i'm dad" in message.content.lower():
            if message.author.id == 756391739056586773:
                name = "joel"
            elif message.author.id == 738980178314657822:
                name = "aditya"
            elif message.author.id == 553871925177221120:
                name = "akhil"
            else:
                name = "bro"
            await message.channel.send(f"Nice innovative joke, {name} ||i appreciate you*'re* sense of grammar||")
        elif "iwabii" in message.content.lower():
            await message.channel.send("Ibrahims at it again lmao")
        elif "ironic" in message.content.lower() and message.author.id == 680298420338294796:
                await message.channel.send("learn to use ironic properly dumbfuck")
                await message.delete()
        elif "fap" in message.content.lower() and message.author.id == 275609153274380289:
                await message.channel.send("Bruh, koshy don't fap again")
        elif "what the fuck did you just fucking say about me, you little bitch?" in message.content.lower():
            await message.channel.send(f"stop. posting. this. it isn't funny, {message.author.mention}")
            await message.delete()
        elif "united states marine corps" in message.content.lower():
            await message.channel.send(f"nice try dumbass, {message.author.mention}")
            await message.delete()
        elif "the storm that wipes out the pathetic little thing you call your life" in message.content.lower():
            await message.channel.send(f"nice try dumbass {message.author.mention}")
            await message.delete()
        elif "that shit to me over the Internet" in message.content.lower():
            await message.channel.send(f"nice try dumbass {message.author.mention}")
            await message.delete()
        elif message.content.startswith('^botservers'):
            await message.channel.send("I'm in " + str(len(self.client.guilds)) + " servers!")
        elif "help with pp" in message.content.lower():
            await message.channel.send("""Good evening, I'm from the National Urology Society and we received your questions sent to our e-mail, and we're pleased to answer:

1) Yes, 3 inches is considered small. We recomend you surgery process;

2) No, it's not usual for the condom to be loose. There's no XS size;

3) Even if 3 inches is quite small, it is still possible for your partner to have an orgasm during sexual relationships, so if it doesn't happen with you like you've mentioned, the lack of competence is your responsibility;

4) No, you cant have a prostate exam, it's only for 50-year-olds or older. Please, do not insist;

5) The attraction for people of the same sex can be a strong sign of homosexuals tendencies;

Any other questions, we're here to help. Have a nice day.""")

def setup(client):
    client.add_cog(aliveabot(client))