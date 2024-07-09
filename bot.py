import discord
from discord.ext import commands

intents = discord.Intents.all() # 請至https://discord.com/developers/applications開啟所有意圖
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    slash = await bot.tree.sync()
    print(f"登入-->{bot.user}\n載入{len(slash)}個斜線指令")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name = "上線囉!"))

@bot.command(name = "測試-回文指令")
async def ctx_test(ctx: commands.Context):
    await ctx.send("這是一個ctx回文指令")

@bot.tree.command(name = "測試-斜線指令-interaction")
async def slash_test_1(interaction: discord.Interaction):
    await interaction.response.send_message("這是一個interaction的斜線指令")



bot.run("TOKEN")
