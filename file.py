import os
import discord
from discord.ext import commands
import random
from time import sleep
from time import *
import random

# Imports Are Done

client = commands.Bot(command_prefix="J", help_command=None)  # Setup The Client Key And Remove The Default Help Command
"""
# Getting This From .env Files By Using OS
T = os.getenv("T")
"""
# Loading Cogs, Cogs Consists Various Commands That We Can Load Unload

try:
    for file in os.listdir('./Cogs'):
        if file.endswith('.py'):
            name = file[:-3]
            client.load_extension(f"Cogs.{name}")

except Exception as e:
    print(f"{name} Can not be loaded")
    raise e

@client.event
async def on_ready():
    # We Need To Know When The Bot Is Online So We Add an 'on_ready' event / function
    print("Bot Is Ready")


@client.command()  # Help Command Seems Fine In The Main File
async def help(ctx):  # Ctx Means Context In The Message
    em = discord.Embed(
        # Embed Is Required To Make The Message More Attractive
        name="Help Command",
        description="",  # Description is not necessary it just takes up a lot of space
        colour=discord.Colour.random(),
        timestamp=ctx.message.created_at  # colour and timestamp are just for decoration
    )

    # Set Author
    em.set_author(name=ctx.author)

    # Set A Footer
    em.set_footer(text="Use 'J' Before Every Command")

    # Add Fields

    em.add_field(name="Jartex Website", value="https://jartexnetwork.com")

    em.add_field(name="Vote For Jartex:", value="https://jartexnetwork.com/vote/")

    em.add_field(name="Jartex Forums:", value="https://jartexnetwork.com/forums/")

    em.add_field(name="Jartex Store:", value="https://store.jartexnetwork.com/")

    em.add_field(name="Jartex Rules:", value="https://jartexnetwork.com/rules/")

    em.add_field(name="Jartex Staff Members:", value="https://jartexnetwork.com/staff/")

    em.add_field(name="How To Join Jartex Network:", value="https://jartexnetwork.com/howtojoin/")

    em.add_field(name="Jartex Server IP:", value="mp.jartexnetwork.com and top.jartex.fun")

    em.add_field(name="Do Jgames", value=" To Know More About Jartex")

    # At Last Send The Embed

    await ctx.send(embed=em)




client.run('Nzk4ODMwODU0NjcwMzg1MjEy.X_6vNQ.meeYGQVKS6aRbWBXBDyv-oEiI_4')  # Bot Token Is The Token That We Imported From .env File By Using OS
