import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
  try:
    synced = await bot.tree.sync()
    print(f'{bot.user} has Connected to Discord !')
    print(f'{str(len(synced))} Commands Synced')
  except Exception as Error:
    print(Error)


@bot.tree.command(name='profile', description='Buy the Demo')
async def profile(interaction: discord.Interaction):
  await interaction.response.send_message(
      f'Your User ID is {interaction.user.id}')


Token = os.environ['TOKEN']
bot.run(Token)
