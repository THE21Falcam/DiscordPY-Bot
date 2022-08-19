import discord
from discord.ext import commands
import asyncio
import os

class DBot (commands.Bot):

  def __init__(self):
    super().__init__(command_prefix = '?', intents = discord.Intents.all(), application_id = 930682541319524352)

  async def setup_hook(self):
    await self.load_extension(f"cogs.levels")
  
  async def on_ready(self):
    print(f'{self.user} has Connected to Discord !')

bot = DBot()
bot.run("Add Your Discord Bot Token Here")
