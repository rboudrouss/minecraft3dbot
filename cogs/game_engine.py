import discord
from discord.ext import commands
from ..secret_things import TESTERS


class GameEngine(commands.Cog):
    def __init__(self, client):
        self.client = client

    # events

    # commands

    @commands.command(aliases=['glv'])
    async def loaded_verif(self, ctx):
        if ctx.author.id in TESTERS:
            await ctx.send('RAS !')

    @commands.command(aliases=[])
    async def init(self, ctx, number: int):
        await ctx.send(':smile:'*number)


def setup(client):
    client.add_cog(GameEngine(client))


# number = 10 if number else number
    # embed = discord.Embed(
    #     title="title",
    #     description='description',
    #     colour=discord.Colour.blue(),
    # )
    # embed.set_footer(
    #     text='footer',
    #     icon_url="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
    # )
    # embed.set_image(
    #     url="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")
    # embed.set_thumbnail(
    #     url="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")
    # embed.set_author(
    #     name="Author Name",
    #     icon_url="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
    # )
    # print("test")
    # await client.say(embed=embed)
