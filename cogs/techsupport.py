import discord
import sys
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
import random
from math import *
import os
from discord.ext.commands.converter import MemberConverter
import asyncio
 

class TechSupport(commands.Cog, description = "Tech-support"):

    def __init__(self,client): 
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Tech Support has been turned on {self.client.user}')
     
    @commands.command(aliases = ["tech", "support"], brief = "Get premium tech-support", help = "")
    async def techsupport(self, ctx):
        devices = ['Automated Dildo', 'Vibrator', 'Automatic Pet Feeder', "PlayStation 2"]
        device = random.choice(devices)
        await ctx.send(f"Good day Sir/Madam, Thank you for calling tech-support regarding your {device}")
        await ctx.send("Please choose your problem from the following options: (enter the number)")
        def check(message):
            return (message.content.lower() == "y" or message.content.lower() == 'n') and message.author == ctx.author 
        async def loading():
            await ctx.send(f"Please wait patiently while we connect you to our specialists")
            await asyncio.sleep(5)
            await ctx.send(f"Our Helpers are busy at the moment, We will get to you in a minute")
            await asyncio.sleep(5)
            await ctx.send(f"Please consider checking the manual or our support forums for a solution before calling us")
        async def reconnect():
            await ctx.send(f"""Connection has been lost
            Would you like to try to reconnect? (y/n)""")
        def check1(message):
            return (message.content == "1" or message.content == '2' or message.content == '3') and message.author == ctx.author 
        if device == "Automated Dildo":
            await ctx.send("""`1) Dildo not extending
2) Dildo not as sensual as before
3) I think my dildo is alive`""")      
            choice = (await self.client.wait_for('message', check=check)).content 
            await ctx.send("Connecting... <a:loading:894873095737856010>")
            await loading()
            await reconnect()
            option = (await self.client.wait_for('message', check=check1)).content 
            if option.lower() == "y":
                await loading()
                if choice == "1":
                    solve = discord.Embed(title = "Solution", description = "Stroke dildo soothingly")
                    await ctx.send(embed = solve)
                elif choice == "2":
                    solve = discord.Embed(title = "Solution", description = "Apply lube or check for dents in dildo")
                    await ctx.send(embed = solve)
                elif choice == "3":
                    solve = discord.Embed(title = "Solution", description = "WHATEVER YOU DO, DO NOT FEED IT")
                    await ctx.send(embed = solve)
                await asyncio.sleep(2)
                await ctx.send("Thank you for reaching out to us, call disconnected")
            elif option.lower() == "n":
                await ctx.send("Call disconnected")
        elif device == "Automatic pet feeder":
            await ctx.send("""`1) Pet not eating`
2) Food smells weird`""")      
            choice = (await self.client.wait_for('message', check=check)).content 
            await ctx.send("Connecting... <a:loading:894873095737856010>")
            await loading()
            await reconnect()
            option = (await self.client.wait_for('message', check=check1)).content 
            if option.lower() == "y":
                await loading()
                if choice == "1":
                    solve = discord.Embed(title = "Solution", description = "Forcefeed the pet until it begs for mercy")
                    await ctx.send(embed = solve)
                elif choice == "2":
                    solve = discord.Embed(title = "Solution", description = "Food is produced by our trustworthy partner PetFudz. Do not worry if pet starts vomitting, throw pet away")
                    await ctx.send(embed = solve)
                elif choice == "3":
                    await ctx.send("That's not a real problem you nitwit")
                await asyncio.sleep(2)
                await ctx.send("Thank you for reaching out to us, call disconnected")
            elif option.lower() == "n":
                await ctx.send("Call disconnected")

        elif device == "PlayStation 2":
            await ctx.send("""`1) PS2 not starting up
2) PS2 having display error
3) PS2 is making a ticking noise`""")    
            choice = (await self.client.wait_for('message', check=check)).content 
            await ctx.send("Connecting... <a:loading:894873095737856010>")
            await loading()
            await reconnect()
            option = (await self.client.wait_for('message', check=check1)).content 
            if option.lower() == "y":
                if choice == "1":
                    solve = discord.Embed(title = "Solution", description = "Plug PS2 into power socket and press power button")
                    await ctx.send(embed = solve)
                elif choice == "2":
                    solve = discord.Embed(title = "Solution", description = "Make sure PS2 not connected to microwave display")
                    await ctx.send(embed = solve)
                elif choice == "3":
                    solve = discord.Embed(title = "Solution", description = "Quick, take PS2 and enter World Trade Centre")
                    await ctx.send(embed = solve)
                await asyncio.sleep(2)
                await ctx.send("Thank you for reaching out to us, call disconnected")
            elif option.lower() == "n":
                await ctx.send("Call disconnected")

    



def setup(client):
    client.add_cog(TechSupport(client))