import asyncio
import discord
from discord.ext import commands

class MemeCaster(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def neat(self, ctx):
        await ctx.send("Neat")
        await asyncio.sleep(0.3)
        await ctx.send("Like")
        await asyncio.sleep(0.5)
        await ctx.send("***ALICE!?!?!?!?!?***")

    @commands.command()
    @commands.guild_only()
    async def sade(self, ctx):
        embed = discord.Embed(title="***MemeCaster!***", color=0xf915d1)
        embed.add_field(name="\"Now im sade\"", value="-kozankun 2k17", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def look(self, ctx):
        embed = discord.Embed(title="***MemeCaster!***", color=0xf915d1)
        embed.add_field(name="\"Use the force look!\"", value="-CloudiamondHD 2017", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="1110")
    @commands.guild_only()
    async def eleven(self, ctx):
        embed = discord.Embed(title="***MemeCaster!***", color=0xf915d1)
        embed.add_field(name="\"11/10 Would do that\"", value="-Luna01H 2017", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def ripa(self, ctx):
        embed = discord.Embed(title="***MemeCaster!***", color=0xf915d1)
        embed.add_field(name="\"Ripa\"", value="-QueenLadz 2017", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def bya(self, ctx):
        embed = discord.Embed(title="***MemeCaster!***", color=0xf915d1)
        embed.add_field(name="\"Bya\"", value="-CloudiamondHD 2017", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def coock(self, ctx):
        embed = discord.Embed(title="***MemeCaster!***", color=0xf915d1)
        embed.add_field(name="\"How to \'coock\' noodles\"", value="-Fearix 2017", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def gadi(self, ctx):
        embed = discord.Embed(title="***MemeCaster!***", color=0xf915d1)
        embed.add_field(name="\"Deez Nuts \'gadi\' \"", value="-Fearix 2017", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="pev")
    @commands.guild_only()
    @commands.has_role("Administrator")
    async def everyone(self, ctx):
        await ctx.message.delete()
        await asyncio.sleep(0.1)
        await ctx.send("@everyone")

    @everyone.error
    async def everyone_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You don't have the \"Admin\" role!")

def setup(bot):
    bot.add_cog(MemeCaster(bot))
