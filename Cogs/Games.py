import discord
from discord.ext import commands


# We Have To Import The Required Modules

class games(commands.Cog):

    # Make A Class, In This Case We Are Making a Games Command

    def __init__(self, client):
        self.client = client

        # Setup The Client Atrribute That We Made In Our Main File

    @commands.command()
    # Commands Need A Decorator
    async def games(self, ctx):
        # If You Are Working In A Class Theb Self Is Must In Every Parentheses

        em = discord.Embed(
            name="Games In Jartex Network",
            description="",
            colour=discord.Colour.random(),
            timestamp=ctx.message.created_at
        )

        em.set_author(name=f"{ctx.author}")

        em.set_footer(text="Play On Jartex! IP: top.jartex.fun")

        em.add_field(name="Bedwars",
                     value="Bedwars Is A Popular Game Containing 4 Different Gamemodes solos, duos, triples, quads. Know More About Bedwars: https://youtu.be/EeN85KwD0PQ")

        em.add_field(name="Skywars",
                     value="Skywars Is Just Like Bedwars Except You Have Only OneLife, gather Stuff be More Powerfull And Win The Game! Know More About Skywars: https://youtu.be/XObfEJ6njMo")

        em.add_field(name="Prison",
                     value="The prison is simple. When you join, you are going to start off at A and you're going to make it all the way to Z. There are prestige to reset your rank and try again. There are warps for your mines, some of them are locked because you haven't reached them yet. watch A Video On Prison: https://youtu.be/H6H424OcP-g ")

        em.add_field(name="Factions",
                     value="Factions is a survival/pvp-based plugin. In the world of factions, you are allowed to kill and steal loot for your own. You are in a clan (or faction), and you fight to grow your faction and base. You are a team with your faction, and you are either neutral, allied, truced, or enemies to any other factions. You protect and expand your factions land, and strive to become the richest and most powerful clan out there. Know More About Factions - https://jartexnetwork.com/threads/factions-beginners-guide.36617/ .  watch a video on factions: https://youtu.be/9EMGgaWtotw")

        em.add_field(name="The Bridge",
                     value="You Start With Nothing, You Have To Work Your Way Up, each team has their own nexus, gear uo and try to damage the nexus of other team, if the health of the nexus of the opposite team is below 0 then your team wins! But dont forget to Protect your nexus From Enemy Team. | watch a video on TheBridge Game: https://youtu.be/l1cwdknGrxc")

        em.add_field(name="SkyBlock",
                     value="Jartex Skyblock, where you can build a new island, leveling up and do some chores! Jartex Server Is Always Updating espically Skyblocks! Many updates changes everything, and certainly makes the game a lot more fun!")

        em.add_field(name="Survival",
                     value="Survival Is Just Like Your Normal Survival But With More Buffs! Survival Has Auction, You Can Make Teams Build With Your Friends And Battle For Stuff! The Survival Has Its Own Server To Reduce The Lag In The Survival Section!")

        em.add_field(name="Practice",
                     value="Want To Enhance Your Skill? Then The practice server is just for you! practice debuff, nodebuff, sumo, combo, gapple and many more!")

        em.add_field(name="Creative",
                     value="Build Some Awesome Builds, Dont Feel Motivated? Go And Take Some Inspiration From Other Builders, Creative Is All About Building and competing, Build With Your Friends, compete against your friends! But Most Importantly Have Fun!")

        await ctx.send(embed=em)


def setup(client):
    client.add_cog(games(client))
