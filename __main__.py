import discord
from discord.ext import commands

import constants

bot = commands.Bot(command_prefix=constants.prefix)

for cog in constants.cogs:
    try:
        bot.load_extension(f"cogs.{cog}")
        print(f"loaded {cog}")
    except Exception as e:
        exc = '{}: {}'.format(type(e).__name__, e)
        print(f"Failed to load extension {cog}\n{exc}")

print(constants.token)
bot.run(constants.token)