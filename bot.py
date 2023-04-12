import discord
from discord.ext import commands
from dotenv import dotenv_values
from m_api import *

config = dotenv_values(".env")

PREFIX = str(config['PREFIX'])

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix=PREFIX, intents=intents)

@client.event
async def on_ready():
    print('{0.user} logged in'.format(client))

    await client.load_extension("extensions.welcomebot")

@client.command()
async def ping(ctx):
    """ Answers with pong """
    await ctx.send("pong")
    print(PREFIX + "ping command executed")

@client.command()
async def math(ctx, *args):
    """ Does math """
    equation = "".join(args)
    answer = eval(equation)
    await ctx.send(" ".join(equation + "=" + str(answer)))
    print(PREFIX + "math command executed")

@client.command()
async def hey(ctx, *args):
    """ Hey there """
    argsArray = list(args)
    if len(argsArray) == 0:
        await ctx.send(f"Hey!")
        print(PREFIX + "hey command executed")
        return
    if argsArray[0] == "dad":
        joke = getDadJoke()
        await ctx.send(joke)
        print("\"" + PREFIX + "hey dad\" command executed")

@client.command()
async def quote(ctx):
    quote = getQuote()
    await ctx.send(quote)
    print(PREFIX + "inspire command executed")

@client.command()
async def cats(ctx):
    pic = getCatPic()
    await ctx.send(pic)
    print(PREFIX + "cats command executed\nURL: " + pic)

@client.command()
async def cat(ctx):
    pic = getCatPic()
    await ctx.send(pic)
    print(PREFIX + "cats command executed\nURL: " + pic)

@client.command()
async def joke(ctx):
    joke = getJoke()
    await ctx.send(joke)
    print(PREFIX + "joke command executed")

@client.command()
async def gif(ctx, *args):
    argsArray = list(args)
    gif = getGif(argsArray)
    await ctx.send("Powered by Giphy\n" + gif)
    print(PREFIX + "gif command executed\nURL: " + gif)

client.run(str(config['TOKEN']), root_logger=True)

