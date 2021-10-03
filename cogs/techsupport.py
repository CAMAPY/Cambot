import discord
import sys
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
import random
from math import *
import os
from discord.ext.commands.converter import MemberConverter
 

class TechSupport(commands.Cog, description = "Tech-support"):

    def __init__(self,client): 
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Tech Support has been turned on {self.client.user}')
     
    @commands.command(aliases = ["tech", "support"], brief = "Get premium tech-support", help = "")
    async def techsupport(self, ctx):
        devices = ['Automated Dildo', 'Vibrator', 'Automatic Pet Feeder', "PlayStation 2", "Smart Watch"]
        device = random.choice(devices)
        await ctx.send(f"Good day Sir/Madam, Thank you for calling tech-support regarding your {device}")
        await ctx.send("Please choose your problem from the following options: (enter the number)")
        if device == "Automated Dildo":
            await ctx.send("""1)Dildo not extending
2)Dildo not as sensual as before
3)I think my dildo is alive""")      
        def check(message):
            return message.content=="1" or message.content.lower() == '2' or message.content.lower() == '3' and message.author == ctx.author  
        choice = (await self.client.wait_for('message', check=check)).content 
        responses = ["Please wait patiently while we connect you to our specialists", "Our Helpers are busy at the moment, We will get to you in a minute", "Please consider checking the manual or our support forums for a solution before calling us"]
        await ctx.send(f"{random.choice(responses)}")
        numbers = random.randint(1, 100)
        if numbers > 90:
            if choice == "1":
                await ctx.send("Stroke dildo soothingly")
            if choice == "2":
                await ctx.send("Apply lube or check for dents in dildo")
            if choice == "3":
                await ctx.send("WHATEVER YOU DO, DO NOT FEED IT")
        else:
            await ctx.send("Call disconnected.Please try again later")

    



def setup(client):
    client.add_cog(TechSupport(client))