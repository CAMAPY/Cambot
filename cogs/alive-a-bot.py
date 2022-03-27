import discord
import sys
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
import random
from math import *
import os


class aliveabot(commands.Cog, description = "Responses that make the bot seem alive"):

    def __init__(self,client): 
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'I has been turned on {self.client.user}')

    @commands.Cog.listener()
    async def on_message(self, message): 
        if message.author == self.client.user:
            return 
        elif message.content.startswith(";t"):
            return
        elif "^" in message.content and message.author.id == 398429963990335489:
                await message.reply("your mom's exponential weight gain be like", mention_author = False)
        elif "im" in message.content.lower() and "hi" in message.content.lower():
            if "dad" in message.content.lower():
                if message.author.id == 756391739056586773:
                    name = "joel"
                elif message.author.id == 738980178314657822:
                    name = "aditya"
                elif message.author.id == 553871925177221120:
                    name = "akhil"
                else:
                    name = "bro"
            else:
                return
            await message.reply(f"Nice innovative joke, {name}", mention_author = False)
        elif "cain" in message.content.lower():
            channel = self.client.get_channel(873983296269348884)
            await channel.send(f"{message.content},  by {message.author.name}")
        elif "i'm" in message.content.lower():
            if "dad" in message.content.lower():
                if message.author.id == 756391739056586773:
                    name = "joel"
                elif message.author.id == 738980178314657822:
                    name = "aditya"
                elif message.author.id == 553871925177221120:
                    name = "akhil"
                else:
                    name = "bro"
            else:
                return
            await message.reply(f"Nice innovative joke, {name} ||but i do appreciate your sense of grammar||", mention_author = False)
        elif "iwabii" in message.content.lower():
            await message.reply("Ibrahims at it again lmao", mention_author = False)
        elif "ironic" in message.content.lower() and message.author.id == 680298420338294796:
                await message.reply("learn to use** **ironic properly, dumbfuck", mention_author = False)
        elif "fap" in message.content.lower() and message.author.id == 275609153274380289:
                await message.reply("Bruh, koshy don't fap again", mention_author = False)
        elif "what the fuck did you just fucking say about me, you little bitch?" in message.content.lower():
            await message.reply(f"stop. posting. this. it isn't funny, {message.author.mention}", mention_author = False)
            await message.delete()
        elif "united states marine corps" in message.content.lower():
            await message.reply(f"nice try dumbass, {message.author.mention}", mention_author = False)
            await message.delete()
        elif "the storm that wipes out the pathetic little thing you call your life" in message.content.lower():
            await message.reply(f"nice try dumbass {message.author.mention}", mention_author = False)
            await message.delete()
        elif "that shit to me over the Internet" in message.content.lower():
            await message.reply(f"nice try dumbass {message.author.mention}", mention_author = False)
            await message.delete()
        elif message.content.startswith('^botservers'):
            await message.reply("I'm in " + str((self.client.guilds)) + " servers!")
        elif "help with pp" in message.content.lower():
            await message.reply("""Good evening, I'm from the National Urology Society and we received your questions sent to our e-mail, and we're pleased to answer:
        
1) Yes, 3 inches is considered small. We recomend you surgery process;

2) No, it's not usual for the condom to be loose. There's no XS size;

3) Even if 3 inches is quite small, it is still possible for your partner to have an orgasm during sexual relationships, so if it doesn't happen with you like you've mentioned, the lack of competence is your responsibility;

4) No, you cant have a prostate exam, it's only for 50-year-olds or older. Please, do not insist;

5) The attraction for people of the same sex can be a strong sign of homosexuals tendencies;

Any other questions, we're here to help. Have a nice day.""", mention_author = False)
        elif "canopy" in message.content.lower() and message.author.id == 780498861713653780:
            await message.reply("stfu chreya", mention_author = False)
        elif "kanopy" in message.content.lower() and message.author.id == 780498861713653780:
            await message.reply("stfu chreya ||lmao u wish||", mention_author = False)
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):  
        error = str(error).split(":")[-1]
        error = discord.Embed(title=f"❌Error encountered❌", description=f"{error}", colour = 0x660000) 
        await ctx.send(embed = error)
def setup(client):
    client.add_cog(aliveabot(client))