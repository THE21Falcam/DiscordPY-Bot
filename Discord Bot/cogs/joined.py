import discord
from discord.ext import commands

class joined(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
      #role = discord.utils.get(member.server.roles, id=<role_id>)
      channel = discord.utils.get(member.guild.channels, id=949907770562449428)
      #await commands.add_roles(member, role)
      await channel.send(f"Hello {member.mention} nice to see you!")
    
async def setup(bot):
    await bot.add_cog(joined(bot))