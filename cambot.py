import discord
import sys
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
import random
from math import *
import os
from discord.ext.commands.converter import MemberConverter

intents = discord.Intents.all()

client = commands.Bot(command_prefix = ';', intents=intents, help_command=PrettyHelp(),case_insensitive=True)

@client.event
async def on_ready():
    print(f'Logged on as {client.user}')
    channel = client.get_channel(872371310704066633)
    await channel.send(f"im turned on")
    

@client.command(brief= "Checks bot's ping")
async def ping(ctx):
    print("Pong")
    await ctx.send('The ping\'s at {0} ms'.format(round(client.latency, 10) *1000))

@client.command(aliases=['calc'],brief="It calculates....no-brainer really", help = "Operations include: '+', '-', '*', '/','**', '^','sqrt','log','abs', '%','cmp','log10', 'pow', '//', 'factorial', 'ceil', 'copysign', 'fabs' , 'floor', 'fmod', 'frexp', 'fsumi', 'isinfinite', 'isinf', 'isnan', 'ldexp', 'modf', 'trunc', 'exp', 'expm1', 'log1p', 'log2', 'acos', 'asin', 'atan', 'atan2', 'cos', 'hypot', 'sin', 'tan', 'degrees', 'radians', 'acosh', 'asinh', 'atanh', 'cosh', 'sinh', 'tanh', 'erf', 'erfc', 'gamma', 'lgamma', 'pi', 'e'")
async def calculate(ctx,*,expression):
    print(expression.split('*'))
    print(expression.split('^'))
    print(expression.split('**'))
    print(expression.split('x'))
    expression = expression.replace("^","**")   
    expression = expression.replace("x","*")
    expression = expression.replace("rem", '%')
    
    if ("*" in expression) or ("x" in expression) or ("^" in expression):
        if ("for" in expression) or ("while" in expression):
            await ctx.send("nt u sunuvabich")
            return
        elif (expression.count('**') > 1) or (expression.count('^') > 1) or (expression.count('x') > 1):
            print(expression.count('**'))
            print(expression.count('*'))
            print(expression.count('^'))
            await ctx.send("Please just let me live")
            return
        elif (999 < int(expression.split('**')[0])) or (999 < int(expression.split('**')[-1])):
            await ctx.send("ok man, daddy fixed me")
            return
        elif ('999' in expression.split('*')[0]) or ('999' in expression.split('*')[-1]):
            await ctx.send("ok man, daddy fixed me")
            return
        elif ('999' in expression.split('^')[0]) or ('999' in expression.split('^')[-1]):
            await ctx.send("ok man, daddy fixed me")
            return  
        elif ('999' in expression.split('x')[0]) or ('999' in expression.split('x')[-1]):
            await ctx.send("ok man, daddy fixed me")
            return
    elif "(" in expression:
        if (eval(int(expression.split("(")[-1][:-1])) > 999):
            await ctx.send("bitch i can find where u live")
    await ctx.send(f"{eval(expression)}")

@client.command(aliases = ['dm'])
async def message(ctx, user: discord.Member, *, content):
    kick = discord.Embed(title=f"You've a message ;)", description=f"{content}\nBy: {ctx.author.mention}")
    await user.send(embed = kick)
@client.command(hidden =True)
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f'`{extension}` has been loaded')

@client.command(hidden = True)
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f'`{extension}` has been unloaded')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run('NzY0Nzg5NTUxMzA2MjQ0MTI3.X4LXxg.5PRzypxPXGiao3DaYTYsXn8rmNc')
