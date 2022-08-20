import discord
from discord.ext import commands
import asyncio
import random
import re

time_regex = re.compile(r"(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h": 3600, "s": 1, "m": 60, "d": 86400}

def convert(argument):
    args = argument.lower()
    matches = re.findall(time_regex, args)
    time = 0
    for key, value in matches:
        try:
            time += time_dict[value] * float(key)
        except KeyError:
            raise commands.BadArgument(
                f"{value} is an invalid time key! h|m|s|d are valid arguments"
            )
        except ValueError:
            raise commands.BadArgument(f"{key} is not a number!")
    return round(time)  

class giveaway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role('Moderators')
    async def start(ctx, self, timing, winners: int, *, prize):
      await self.send('Okay, making a giveaway!', delete_after=3)
      gwembed = discord.Embed(
        title="🎉 __**Giveaway**__ 🎉",
        description=f'Prize: {prize}',
        color=0xb4e0fc
  )
      time = convert(timing)
      gwembed.set_footer(text=f"This giveaway ends {time} seconds from this message.")
      gwembed = await self.send(embed=gwembed)
      await gwembed.add_reaction("🎉")
      await asyncio.sleep(time)
      message = await self.fetch_message(gwembed.id)
      users = [user async for user in message.reactions[0].users()]
      if len(users) == 0:
        await self.send("No winner was decided.")
        return
      for i in range(winners):
        winner = random.choice(users)
        await self.send(f"**Congrats to: {winner}!**")
        
async def setup(bot):
    await bot.add_cog(giveaway(bot))