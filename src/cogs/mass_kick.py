from  discord.ext import commands

class MassKick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def masskick(self, ctx):
        await ctx.message.delete()
        Guild = ctx.guild
        if not Guild:
            return False
        
        if not Guild.me.guild_permissions.kick_members:
            await ctx.send("Bot không có quyền kick thành viên.")
            return False

        owner_id = Guild.owner_id
        for member in Guild.members:
            if member.id != owner_id:
                try:
                    await member.kick(reason = 'Nuke by Fuzzy-chan')
                    print(f'>>> Kick thành công {member.name}')
                except Exception as Error_On_Mass_Kick:
                    print(f'>>> Không thể kick {member.name} ^^^{Error_On_Mass_Kick}')

async def setup(bot):
    await bot.add_cog(MassKick(bot))