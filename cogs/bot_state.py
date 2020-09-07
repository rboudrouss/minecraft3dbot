import discord
from discord.ext import commands


class BotState(commands.Cog):
    def __init__(self, client):
        self.client = client

    # events
    # @commands.Cog.listener()
    # async def on_ready(self):
    #     pass

    # commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong !')


def setup(client):

    client.add_cog(BotState(client))
