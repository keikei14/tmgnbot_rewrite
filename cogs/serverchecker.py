from mcstatus import MinecraftServer
from discord.ext import commands
import socket

server = MinecraftServer.lookup("tmgn.g-s.nu:25565")

class ServerChecker:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="status")
    @commands.guild_only()
    async def serverstatus(self, ctx):
        try:
            status = server.status()
        except socket.timeout as error:
            await ctx.send("Cannot connect to server. Maybe server offline?")
            print(error)
        else:
            await ctx.send("The server has {0} players and has a latency of {1}ms.".format(status.players.online, status.latency))

    @commands.command(name="ping")
    @commands.guild_only()
    async def serverping(self, ctx):
        try:
            latency = server.ping()
        except socket.timeout as error:
            await ctx.send("Cannot connect to server. Maybe server offline?")
        else:
            await ctx.send("The server replied in {0} ms.".format(latency))



def setup(bot):
    bot.add_cog(ServerChecker(bot))