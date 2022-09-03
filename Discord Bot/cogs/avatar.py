import discord
from discord.ext import commands

class avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, *,  avamember : discord.Member=None):
        embed = discord.Embed(
          title=f'{avamember.name}\'s Avatar:', color=discord.Colour.red())
        embed.set_image(url=avamember.display_avatar)
        await ctx.send(embed=embed)
      
async def setup(bot):
    await bot.add_cog(avatar(bot))