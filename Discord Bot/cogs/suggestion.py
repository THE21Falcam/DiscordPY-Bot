import discord
from discord.ext import commands

class suggestions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def suggestion(ctx,self, * , content: str):
      title, description= content.split('=')
      Embed = discord.Embed(title=title, description=description, color=0x00ff40)
      channel = self.bot.get_channel(Here)#Enter Channal ID In Which You Want to Put Suggestion
      vote = await channel.send(embed=Embed)
      await vote.add_reaction("✅")
      await vote.add_reaction("❌")
      await self.send("your suggestion has been send")
    
async def setup(bot):
    await bot.add_cog(suggestions(bot))
