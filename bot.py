from secret_things import BOT_TOKEN, TESTERS
import discord
from discord.ext import commands
import os

# bot
client = commands.Bot(command_prefix="+")


# fonctions
def load_cogs():
    print("loading Cogs...")
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
    print("Cogs loaded")


def unload_cogs():
    print("unloading Cogs...")
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.unload_extension(f'cogs.{filename[:-3]}')
    print("Cogs unloaded")


# Events
@client.event
async def on_ready():  # on ready
    load_cogs()

    await client.change_presence(
        status=discord.Status.idle,
        activity=discord.Game('3d mc discord thing'),
    )
    print("\nready\n")


@client.event
async def on_command_error(ctx, error):  # in case of errors
    if isinstance(error, commands.MissingPermissions):
        print(error)
        await ctx.send("Error Missing Permission")


# Commands
@client.command(aliases=['rg'])
async def reload_cogs(ctx):
    if ctx.author.id in TESTERS:
        await ctx.send("`reloading the Cogs...`")
        unload_cogs()
        load_cogs()
        await ctx.send("`Cogs reloaded !`")
    else:
        await ctx.send("Error you are not a tester")


@client.command()
async def stop(ctx):
    quit()


client.run(BOT_TOKEN)
