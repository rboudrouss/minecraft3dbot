import discord
from discord.ext import commands
from game import *
from emoji_generator import *
import os
import sys


class GameFrontEnd(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.game = Game()

    # events

    # commands

    @commands.command(aliases=['glv'])
    async def loaded_verif(self, ctx):
        await ctx.send('RAS !')

    @commands.command(aliases=[])
    async def init(self, ctx, dimensions: tuple):
        await ctx.send(dimensions, type(dimensions))


def setup(client):
    client.add_cog(GameFrontEnd(client))


""" embed model
    number = 10 if number else number
    embed = discord.Embed(
        title="title",
        description='description',
        colour=discord.Colour.blue(),
    )
    embed.set_footer(
        text='footer',
        icon_url="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
    )
    embed.set_image(
        url="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")
    embed.set_thumbnail(
        url="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")
    embed.set_author(
        name="Author Name",
        icon_url="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
    )
    await client.say(embed=embed)
"""
