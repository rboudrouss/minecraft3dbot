import discord
from discord.ext import commands
import numpy as np
import os
import sys
from game import *
from emoji_generator import *
DBEMOJI_EQ = {}


class GameFrontEnd(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.DBEMOJI_EQ = {
            i.name: f"<:{i.name}:{i.id}>" for i in self.client.emojis}

    def discord_message(self):
        demoji_array = self.game.discord_emoji_array()
        text = ''
        for i in range(self.game.shape[0]):
            for j in range(self.game.shape[1]):
                text += self.DBEMOJI_EQ.get(
                    demoji_array[i, j], f"le codeur est débile {demoji_array[i, j]}")
            text += '\n'
        return text

    # events

    # commands

    @commands.command(aliases=['glv'])
    async def loaded_verif(self, ctx):
        await ctx.send('RAS !')

    @commands.command()
    async def emoji(self, ctx):
        for i in self.client.emojis:
            await ctx.send(str(i))

    @commands.command()
    async def init(self, ctx, vdimension=5, hdimension=5):
        self.game = Game((vdimension, hdimension))

        # example actions
        # self.game.selected_move(1, 1)
        # self.game.interact_block(-1)

        # update emojis
        self.game.render_emojis()

        await ctx.send(self.discord_message())

    @commands.command()
    async def move(self, ctx, vmove: int, hmove: int):

        # action
        self.game.selected_move(vmove, hmove)

        # update emojis
        self.game.render_emojis()

        # generate message
        demoji_array = self.game.discord_emoji_array()

        await ctx.send(self.discord_message())

    @commands.command()
    async def interact(self, ctx, type: int):

        # action
        self.game.interact_block(type)

        # update emojis
        self.game.render_emojis()

        # generate message
        demoji_array = self.game.discord_emoji_array()

        await ctx.send(self.discord_message())

    @commands.command()
    async def test(self, ctx, a: int, b: int):
        print(a, b)
        print(type(a), type(b))
        await ctx.send(str(a)+" "+str(b))
        await ctx.send(str(type(a))+" "+str(type(b)))

    @commands.command()
    async def depth(self, ctx):
        await ctx.send("depth array :")
        await ctx.send(str(self.game.get_depth_array()))

    @commands.command()
    async def all_data(self, ctx):
        await ctx.send("depth array :")
        await ctx.send(str(self.game.get_depth_array()))
        await ctx.send("DBEMOJI_EQ :")
        await ctx.send(str(self.DBEMOJI_EQ))
        await ctx.send("DISCORD_EMOJIS_EQ in emoji_generator:")
        await ctx.send(str(DISCORD_EMOJIS_EQ))
        await ctx.send("discord_emoji_array :")
        await ctx.send(str(self.game.discord_emoji_array()))


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
