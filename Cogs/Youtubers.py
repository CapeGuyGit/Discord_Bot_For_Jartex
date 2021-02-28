import discord
import random
from discord.ext import commands

Yt_list = ['Sahvi', 'Cronkers', 'Caddy', 'Joweek', 'Nuqna', 'Everyone']


class Youtubers(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def YT(self, ctx):
        # Just To tell how many youtubers are in Jartex

        em = discord.Embed(
            name="Youtubers In Jartex",
            description="",
            colour=discord.Colour.random(),
            timestamp=ctx.message.created_at

        )

        em.set_author(name=ctx.author)

        em.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)

        em.add_field(name="Sahvi", value="Visit Sahvi's Channel: https://youtube.com/c/Sahvi")

        em.add_field(name="Cronkers", value="Visit Cronker's Channel: https://youtube.com/c/Cronkers")

        em.add_field(name="Caddy", value="Visit Caddy's Channel: https://youtube.com/c/CaddyBouPlayz")

        em.add_field(name="Joweek", value="Visit joweek's channel: https://youtube.com/c/Joweek")

        em.add_field(name="Nuqna", value="Visit Nuqna's Channel: https://youtube.com/c/SluweLama")

        em.add_field(name="My Favourite Youtuber:", value=f"{random.choice(Yt_list)}!")

        em.add_field(name="Dont Forget To Check out Jartex's Discord!", value="https://jartexnetwork.com/discord")

        await ctx.send(embed=em)


def setup(client):
    client.add_cog(Youtubers(client))
