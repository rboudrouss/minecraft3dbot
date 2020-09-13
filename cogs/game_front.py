import discord
from discord.ext import commands
import numpy as np
import os
import sys
from utils.game import *
from utils.secret_things import TESTERS


DBEMOJI_EQ = {}


class GameFrontEnd(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.DBEMOJI_EQ = {
            i.name[:-11]: f"<:{i.name}:{i.id}>" for i in self.client.emojis}

    def discord_message(self):
        emoji_array = self.game.get_emoji_array()
        msg_list = ['']
        index = 0
        for i in range(self.game.shape[0]):
            for j in range(self.game.shape[1]):
                msg_list[0] += self.DBEMOJI_EQ.get(
                    emoji_array[i, j],
                    # hope this won't happen
                    f"le codeur est débile {emoji_array[i, j]}"
                )
            msg_list[0] += '\n'
        if len(msg_list[0]) > 1999:
            msg_list[0] = "Beaucoup trop long"
        return msg_list[0]

    async def add_allreactions(self):
        print("\nadding reactions...")
        await self.message.add_reaction('⬅️')  # arrow left
        await self.message.add_reaction('⬆️')  # arrow up
        await self.message.add_reaction('⬇️')  # arrow down
        await self.message.add_reaction('➡️')  # arrow right
        await self.message.add_reaction('💥')  # collision
        await self.message.add_reaction('➕')  # collision
        print('reactions added !')

    async def move_f(self, vmove, hmove):
        # action
        self.game.selected_move(vmove, hmove)

        # update emojis
        self.game.render_emojis()

        await self.message.edit(content=self.discord_message())

    async def interact_f(self, type):
        # action
        self.game.interact_block(type)

        # update emojis
        self.game.render_emojis()

        await self.message.edit(content=self.discord_message())

    # events
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if self.user != user:
            return
        if reaction.emoji in []:
            try:
                await reaction.remove(user)
            except discord.errors.Forbidden:
                # FIXME
                await self.client.send_message(user, 'An error has occured,\nplease use `move` and `interact` commands instead')
            except:  # TODO find this error => not enough permission
                await self.client.send_message(user, 'I actually need the "manage messages" permission to actually delete the reaction --\'')

        if reaction.emoji == "⬅️":
            await self.move_f(0, -1)
        elif reaction.emoji == "⬆️":
            await self.move_f(-1, 0)
        elif reaction.emoji == "⬇️":
            await self.move_f(1, 0)
        elif reaction.emoji == "➡️":
            await self.move_f(0, 1)
        elif reaction.emoji == "💥":
            await self.interact_f(1)
        elif reaction.emoji == "➕":
            await self.interact_f(-1)

    # commands

    @commands.command(aliases=['start', 'fdp'])
    async def init(self, ctx, vdimension=5, hdimension=5):
        if hdimension > 50:
            hdimension = 50
        # if not vdimension:
        #     vdimension = 5
        # if not hdimension:
        #     hdimension = 5
        self.game = Game((vdimension, hdimension))
        self.user = ctx.author

        # example actions
        # self.game.selected_move(1, 1)
        # self.game.interact_block(-1)

        # update emojis
        self.game.render_emojis()

        self.message = await ctx.send(self.discord_message())
        await self.add_allreactions()

    @commands.command()
    async def move(self, ctx, vmove: int, hmove: int):
        await move_f(vmove, hmove)

    @commands.command()
    async def interact(self, ctx, type: int):
        await interact_f(type)

    @commands.command()
    async def depth(self, ctx):
        if ctx.author.id in TESTERS:
            await ctx.send("depth array :")
            await ctx.send(str(self.game.get_depth_array()))

    @commands.command()
    async def all_data(self, ctx):
        if ctx.author.id in TESTERS:
            await ctx.send("depth array :")
            await ctx.send(str(self.game.get_depth_array()))
            await ctx.send("DBEMOJI_EQ :")
            await ctx.send(str(self.DBEMOJI_EQ))
            await ctx.send("emoji_array :")
            await ctx.send(str(self.game.get_emoji_array()))


def setup(client):
    client.add_cog(GameFrontEnd(client))


""" embed model
    embed = discord.Embed(
        title="title",
        description='description',
        colour=discord.Colour.blue(),
    )
    embed.set_qqch(
    )
    await client.say(embed=embed)
"""
