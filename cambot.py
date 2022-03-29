import discord
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
    operation  = False
    expression = expression.replace("^","**")   
    expression = expression.replace("x","*")
    expression = expression.replace("rem", '%')
    for i in [ '+', '-', '*', '/','**', '^','sqrt','log','abs', '%','cmp','log10', 'pow', '//', 'factorial', 'ceil', 'copysign', 'fabs' , 'floor', 'fmod', 'frexp', 'fsumi', 'isinfinite', 'isinf', 'isnan', 'ldexp', 'modf', 'trunc', 'exp', 'expm1', 'log1p', 'log2', 'acos', 'asin', 'atan', 'atan2', 'cos', 'hypot', 'sin', 'tan', 'degrees', 'radians', 'acosh', 'asinh', 'atanh', 'cosh', 'sinh', 'tanh', 'erf', 'erfc', 'gamma', 'lgamma', 'pi', 'e']:
        if i in expression:
            operation = True
    
    if ("*" in expression) or ("x" in expression) or ("^" in expression):
        if ("for" in expression) or ("while" in expression or ("factorial" in expression) or ("eval" in expression)):
            await ctx.send("nt u sunuvabich")
            return
        else:
            num = ""
            for i in expression:
                if i.isdigit():
                    num += i
                else:
                    break
            print(num)
            if int(num) > 9999:
                num = ""
                await ctx.send("-_-")
                return
            num = ""
            print("ok bro", expression[::-1])
            for i in expression[::-1]:
                if i.isdigit():
                    num += i
                    print(num)
                else:
                    break
            print(num)
            if int(num[::-1]) > 9999:
                await ctx.send("-_-")
                return
    elif operation == False:
        await ctx.send("Please enter a valid operation")
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
