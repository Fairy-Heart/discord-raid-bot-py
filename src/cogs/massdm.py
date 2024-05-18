from discord.ext import commands



class MassDm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def massdm(self, ctx):
        Guild = ctx.guild

        if not Guild:
            return False


        content_spam = "Damn mtf ???"  # sửa cái này thành bất cứ thành cái gì 
        # mà bạn muốn spam 
        for member in Guild.members:
            try:
                await member.send(content_spam)
                print(f'>>> SEND DM FOR {member.name}')

            except Exception as Error_On_MassDM:
                print(f'>>> Có lỗi xảy ra khi mass DM {member.name} ^^^{Error_On_MassDM}')

async def setup(bot):
    await bot.add_cog(MassDm(bot))