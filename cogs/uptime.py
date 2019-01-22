import datetime
import time

from discord.ext import commands

start_time = time.time()

class UptimeCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def uptime(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        await ctx.send("Current uptime: " + text)

def setup(bot):
    bot.add_cog(UptimeCog(bot))