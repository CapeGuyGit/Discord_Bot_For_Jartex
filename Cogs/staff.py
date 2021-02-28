import discord
from discord.ext import commands
import os


class Staff(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def staff(self, ctx):
        em = discord.Embed(
            name="All The Staff Members And Owner",
            descriptiom="",
            colour=discord.Colour.random(),
            timestamp=ctx.message.created_at
        )

        em.set_author(name=f"{ctx.author}")
        em.set_footer(text=f"requested By: {ctx.author}")

        em.add_field(name="owners Of The Server:", value=f"voodootje0 and Max")
        em.add_field(name="Developers:", value=f"JustThiemo and Botervrij")

        em.add_field(name="Senior Moderators:", value=f" Pace and Rodagave115")
        em.add_field(name="Moderators:", value=f"Viclyn_, natty_sword, k4otIc_girl, NotSansy, hakim251, Mayak_123, chocz700, xd_banana")

        em.add_field(name="Junior Moderators",value=f"DrogonMC, LagginMC, MoudTage_, Knowly, Ichmagmiri, JoltTheBolt, ZoneRGH")
        em.add_field(name="Helpers:", value=f"GeorgeAWP, Tyrelle, Unalert, ovq, Nightwave_YT, Sweazi, EvilDrago12, SanadBilleh, zethfull, babyplatypus")

        em.add_field(name="Trial Moderators:", value=f"doggies2000004, NotLoLo1818, Mykkull")

        await ctx.send(embed=em)


def setup(client):
    client.add_cog(Staff(client))
