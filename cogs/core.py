import discord
from discord.ext import commands

import checks


class Core(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @commands.command(checks=[checks.in_command_cahnnel])
    async def test(self, ctx):
        await ctx.send("online")


def setup(bot: commands.Bot):
    bot.add_cog(Core(bot))
