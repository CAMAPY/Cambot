import discord
import sys
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
import random
from math import *
import os
from discord.ext.commands.converter import MemberConverter

intents = discord.Intents.all()

client = commands.Bot(command_prefix = ';', intents=intents, help_command=PrettyHelp())

@client.event
async def on_ready():
    print(f'Logged on as {client.user}')



@client.command(aliases=["t"],brief="Literally just replies with whats in your message after the command")
async def test(ctx,*, arg):
    await ctx.send(arg)
    channel = client.get_channel(872371310704066633)
    await channel.send(f"{arg}, requested by {ctx.author.name}")
    await ctx.message.delete()



@client.command(brief= "Checks bot's ping", hidden = True)
async def ping(ctx):
    print("Pong")
    await ctx.send('The ping\'s at {0} ms'.format(round(client.latency, 10) *1000))



@client.event()
async def on_message(message): 
    possible_responses = [ 'hello', 'suppers', 'yo wassup', 'stfu dumbass', 'what do u want this time?', 'ok now what?', 'hello daddy :drooling_face:' ] 
    if "cambot" in message.content.lower():
        await message.channel.send(f"{random.choice(possible_responses)} {message.author.mention}")
    await client.process_commands(message)

@client.event()
async def on_message(message):  
    if "^" in message:
        if message.author.id == 398429963990335489:
            await message.channel.send("your mom's exponential weight gain be like")
    await client.process_commands(message)







@client.command(aliases=['calc'],brief="It calculates....no-brainer really", help = "Operations include: '+', '-', '*', '/','**', '^','sqrt','log','abs', '%','cmp','log10', 'pow', '//', 'factorial', 'ceil', 'copysign', 'fabs' , 'floor', 'fmod', 'frexp', 'fsumi', 'isinfinite', 'isinf', 'isnan', 'ldexp', 'modf', 'trunc', 'exp', 'expm1', 'log1p', 'log2', 'acos', 'asin', 'atan', 'atan2', 'cos', 'hypot', 'sin', 'tan', 'degrees', 'radians', 'acosh', 'asinh', 'atanh', 'cosh', 'sinh', 'tanh', 'erf', 'erfc', 'gamma', 'lgamma', 'pi', 'e'")
async def calculate(ctx,*,expression):
    expression = expression.replace("^","**")   
    expression = expression.replace("x","*")
    expression = expression.replace("rem", '%')
    await ctx.send(f"{eval(expression)}")
        


@client.command(brief='Renames the bot (only for owner)', hidden = True)
@commands.is_owner()
async def rename(name):
    await client.user.edit(username=name)


@client.event()
async def on_message(message):  
    if "ironic" in message.content.lower():
        if message.author.id == 578865305632243712:
            await message.channel.send("Learn to use `ironic` properly u dumbfuck")
    await client.process_commands(message)


@client.event()
async def on_message(message):  
    if "fap" in message.content.lower():
        if message.author.id == 275609153274380289:
            await message.delete()
            await message.channel.send("Bruh, koshy don't fap again")
    await client.process_commands(message)


@client.command(aliases=["s"], brief='Changes the bot\'s playing status.', hidden =True)
@commands.is_owner()
async def status(ctx, *, status=''):            #im the 
    # if status == None:
    #         status = ''
    await client.change_presence(status=discord.Status.online, activity=discord.Game(status))
    await ctx.send(f'launching {status}.')




@client.command(aliases=["quit", "q"], brief="Shuts down bot (Only for owner)", hidden = True)
@commands.is_owner()
async def close(ctx):
    await ctx.send(f"Ok bye! :wave:")
    await client.close()
    print("Ok bye! :wave:")


@client.command(hidden =True)
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f'{extension} has been loaded')

@client.command(hidden = True)
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f'{extension} has been unloaded')



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run('NzY0Nzg5NTUxMzA2MjQ0MTI3.X4LXxg.-Y3V9dnW6IHl2hbrdrUah9xzcLA')
