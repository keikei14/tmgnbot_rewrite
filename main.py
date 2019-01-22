import discord
import private_stuff
import os
from discord.ext import commands

prefix = "$"

bot = commands.Bot(command_prefix=prefix, description="YEET")

startup_extensions = os.listdir("./cogs")
if "__pycache__" in startup_extensions:
    startup_extensions.remove("__pycache__")
startup_extensions = [ext.replace('.py', '') for ext in startup_extensions]
loaded_extensions = []

bot.remove_command("help")


@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    game = discord.Game("with you <3")
    await bot.change_presence(status=discord.Status.online, activity=game)

    print("Loading {} extension(s)...".format(len(startup_extensions)))

    for extension in startup_extensions:
        try:
            bot.load_extension("cogs.{}".format(extension.replace(".py", "")))
            loaded_extensions.append(extension)

        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n\t->{}'.format(extension, exc))
    print('Successfully loaded the following extension(s): {}'.format(loaded_extensions))


@bot.command()
async def hi(ctx):
    await ctx.send("Hi {0.author}!".format(ctx))

@bot.command()
async def help(ctx):
    await ctx.send("Available commands:\n{0}help\n{0}uptime\n{0}neat\n{0}sade\n{0}ripa\n{0}hi\n{0}bya".format(prefix))

bot.run(private_stuff.token, bot=True, reconnect=True)