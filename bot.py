from utils.secret_things import BOT_TOKEN, TESTERS
import discord
from discord.ext import commands
import os
import sys

# TODO add documentation

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

    await client.change_presence(
        status=discord.Status.idle,
        activity=discord.Game('Loading cogs...'),
    )

    try:
        load_cogs()
    except commands.errors.ExtensionAlreadyLoaded:
        pass

    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Game('3d mc discord thing'),
    )
    print("\nready\n")


# Commands

@client.command(aliases=['rc'])
async def reload_cogs_(ctx):
    if ctx.author.id in TESTERS:
        await client.change_presence(
            status=discord.Status.idle,
            activity=discord.Game('reloading cogs...'),
        )
        await ctx.send("`reloading Cogs...`")

        unload_cogs()
        load_cogs()

        await client.change_presence(
            status=discord.Status.online,
            activity=discord.Game('3d mc discord thing'),
        )
        await ctx.send("`Cogs reloaded !`")
    else:
        await ctx.send("Error you are not a tester :p")


@client.command(aliases=['lc'])
async def load_cogs_(ctx):
    if ctx.author.id in TESTERS:
        await client.change_presence(
            status=discord.Status.idle,
            activity=discord.Game('reloading cogs...'),
        )
        await ctx.send("`loading Cogs...`")

        load_cogs()

        await client.change_presence(
            status=discord.Status.online,
            activity=discord.Game('3d mc discord thing'),
        )
        await ctx.send("`Cogs loaded !`")
    else:
        await ctx.send("Error you are not a tester :p")


@client.command(aliases=['uc'])
async def unload_cogs_(ctx):
    if ctx.author.id in TESTERS:
        await client.change_presence(
            status=discord.Status.idle,
            activity=discord.Game('reloading cogs...'),
        )
        await ctx.send("`Unloadging Cogs...`")

        unload_cogs()
        load_cogs()

        await client.change_presence(
            status=discord.Status.online,
            activity=discord.Game('3d mc discord thing'),
        )
        await ctx.send("`Cogs unloaded !`")
    else:
        await ctx.send("Error you are not a tester :p")


@client.command(aliases=['quit', 'yeet'])
async def stop(ctx):
    await ctx.send("`quitting...`")
    quit()


client.run(BOT_TOKEN)
