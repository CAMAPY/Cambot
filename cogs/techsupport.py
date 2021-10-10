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
        number = random.randint(1,101)
        await ctx.send(f"Good day Sir/Madam, Thank you for calling tech-support regarding your {device}")
        await ctx.send("Please choose your problem from the following options: (enter the number)")
        
        def check1(message):
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
        def check(message):
            return (message.content == "1" or message.content == '2' or message.content == '3') and message.author == ctx.author 
        
        if device == "Automated Dildo":
            await ctx.send("""`1) Dildo not extending
2) Dildo not as sensual as before
3) I think my dildo is alive`""")      
            choice = (await self.client.wait_for('message', check=check)).content 
            await ctx.send("Connecting... <a:loading:894873095737856010>")
            await loading()
            if number > 80:
                if choice == "1":
                    solve = discord.Embed(title = "Solution", description = "Stroke dildo soothingly\nProblem: Dildo not extending")
                elif choice == "2":
                    solve = discord.Embed(title = "Solution", description = "Apply lube or check for dents in dildo\nProblem: Dildo not as sensual as before")
                elif choice == "3":
                    solve = discord.Embed(title = "Solution", description = "WHATEVER YOU DO, DO NOT FEED IT\nProblem: I think my dildo is alive")
                await ctx.send(embed = solve)
                await asyncio.sleep(2)
                await ctx.send("Thank you for reaching out to us, call disconnected")
            else:
                await reconnect()
                option = (await self.client.wait_for('message', check=check1)).content 
                if option.lower() == "y":
                    await loading()
                    if choice == "1":
                        solve = discord.Embed(title = "Solution", description = "Stroke dildo soothingly\nProblem: Dildo not extending")
                    elif choice == "2":
                        solve = discord.Embed(title = "Solution", description = "Apply lube or check for dents in dildo\nProblem: Dildo not as sensual as before")
                    elif choice == "3":
                        solve = discord.Embed(title = "Solution", description = "WHATEVER YOU DO, DO NOT FEED IT\nProblem: I think my dildo is alive")
                    await ctx.send(embed = solve)
                    await asyncio.sleep(2)
                    await ctx.send("Thank you for reaching out to us, call disconnected")
                elif option.lower() == "n":
                    await ctx.send("Call disconnected")

        elif device == "Automatic Pet Feeder":
            await ctx.send("""`1) Pet not eating food
2) Food smells weird`""")      
            choice = (await self.client.wait_for('message', check=check)).content 
            await ctx.send("Connecting... <a:loading:894873095737856010>")
            await loading()
            if number > 80:
                if choice == "1":
                    solve = discord.Embed(title = "Solution", description = "Force feed the pet until it begs for mercy\nProblem: Pet not eating food")
                    await ctx.send(embed = solve)
                elif choice == "2":
                    solve = discord.Embed(title = "Solution", description = "Food is produced by our trustworthy partner PetFudz. Do not worry if pet starts vomitting, throw pet away\nProblem: Food smells weird")
                    await ctx.send(embed = solve)
                elif choice == "3":
                    await ctx.send("That's not a real problem you nitwit")
                await asyncio.sleep(2)
                await ctx.send("Thank you for reaching out to us, call disconnected")
            else:
                await reconnect()
                option = (await self.client.wait_for('message', check=check1)).content 
                if option.lower() == "y":
                    await loading()
                    if choice == "1":
                        solve = discord.Embed(title = "Solution", description = "Force feed the pet until it begs for mercy\nProblem: Pet not eating food")
                        await ctx.send(embed = solve)
                    elif choice == "2":
                        solve = discord.Embed(title = "Solution", description = "Food is produced by our trustworthy partner PetFudz. Do not worry if pet starts vomitting, throw pet away\nProblem: Food smells weird")
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
            if number > 80:
                if choice == "1":
                    solve = discord.Embed(title = "Solution", description = "Plug PS2 into power socket and press power button\nProblem: PS2 not starting up")
                elif choice == "2":
                    solve = discord.Embed(title = "Solution", description = "Make sure PS2 not connected to microwave display\nProblem: PS2 having display error ")               
                elif choice == "3":
                    solve = discord.Embed(title = "Solution", description = "Quick, take PS2 and enter World Trade Centre\nProblem: PS2 is making a ticking noise")
                await ctx.send(embed = solve)
                await asyncio.sleep(2)
                await ctx.send("Thank you for reaching out to us, call disconnected")
            else:
                await reconnect()
                option = (await self.client.wait_for('message', check=check1)).content 
                if option.lower() == "y":
                    await loading()
                    if choice == "1":
                        solve = discord.Embed(title = "Solution", description = "Plug PS2 into power socket and press power button\nProblem: PS2 not starting up")
                        await ctx.send(embed = solve)
                    elif choice == "2":
                        solve = discord.Embed(title = "Solution", description = "Make sure PS2 not connected to microwave display\nProblem: PS2 having display error ")
                        await ctx.send(embed = solve)
                    elif choice == "3":
                        solve = discord.Embed(title = "Solution", description = "Quick, take PS2 and enter World Trade Centre\nProblem: PS2 is making a ticking noise")
                        await ctx.send(embed = solve)
                    await asyncio.sleep(2)
                    await ctx.send("Thank you for reaching out to us, call disconnected")
                elif option.lower() == "n":
                    await ctx.send("Call disconnected")

        elif device == "Vibrator":
            await ctx.send("""1)Vibrator not vibing
2)Vibrator wailing in flawless russian
3)I think my vibrator is a serial killer""")
            choice = (await self.client.wait_for('message', check=check)).content 
            await ctx.send("Connecting... <a:loading:894873095737856010>")
            await loading()
            if number > 80:
                if choice == "1":
                    solve = discord.Embed(title = "Solution", description = "Play `Vennu Mallesh - Its My Life What Ever I Wanna Do` 10 times a day until vibing has reached optimal level\nProblem: Vibrator not vibing")
                elif choice == "2":
                    solve = discord.Embed(title = "Solution", description = "Play russian national anthem on JBL Charge 5\n Problem: Vibrator wailing in flawless russian")              
                elif choice == "3":
                    solve = discord.Embed(title = "Solution", description = "What are you waiting for? Show it a list of kpop fans\n Problem: I think my vibrator is a serial killer    ")
                await ctx.send(embed = solve)
                await asyncio.sleep(2)
                await ctx.send("Thank you for reaching out to us, call disconnected")
            else:
                await reconnect()
                option = (await self.client.wait_for('message', check=check1)).content 
                if option.lower() == "y":
                    await loading()
                    if choice == "1":
                        solve = discord.Embed(title = "Solution", description = "Play `Vennu Mallesh - Its My Life What Ever I Wanna Do` 10 times a day until vibing has reached optimal level\nProblem: Vibrator not vibing")
                    elif choice == "2":
                        solve = discord.Embed(title = "Solution", description = "Play russian national anthem on JBL Charge 5\n Problem: Vibrator wailing in flawless russian")              
                    elif choice == "3":
                        solve = discord.Embed(title = "Solution", description = "What are you waiting for? Show it a list of kpop fans\n Problem: I think my vibrator is a serial killer    ")
                    await ctx.send(embed = solve)
                    await asyncio.sleep(2)
                    await ctx.send("Thank you for reaching out to us, call disconnected")
                elif option.lower() == "n":
                    await ctx.send("Call disconnected")



    



def setup(client):
    client.add_cog(TechSupport(client))