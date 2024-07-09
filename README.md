# 使用Discord.py製作一隻簡易的機器人

這個檔案可以讓機器人擁有回文指令和斜線指令並且只需單一python檔案

<hre>

檔案中的TOKEN需換成自己的，請至[Discord Developer Portal](https://discord.com/developers/applications)取得

```bash
pip install discord.py
```

替換方法如下:
```py
# 最後一行
bot.run("TOKEN")
```

將TOKEN換成自己的，例如:

我的TOKEN是 MjU3NTEzNDY1Mzk2ODYxNTc5.XzmDDf.FwroWLrnjuQAUQvtN2PIIHB5hoi
```py
# 最後一行
bot.run("MjU3NTEzNDY1Mzk2ODYxNTc5.XzmDDf.FwroWLrnjuQAUQvtN2PIIHB5hoi")
```

也需要在[Discord Developer Portal](https://discord.com/developers/applications)操作以下步驟

**1.點擊此區**

<img width="266" alt="image" src="https://github.com/catchen541/discordpy-simple-bot/assets/131455122/fb674939-90da-4b4c-a1a2-2fdab874c969">


**2.開啟三個按鈕**
<img width="628" alt="image" src="https://github.com/catchen541/discordpy-simple-bot/assets/131455122/a2ead4bb-d023-4870-9e2a-7142c4b1d01d">

**3.啟動機器人即可**

# 大致上運作原理

*導入所需模組*
```py
import discord
from discord.ext import commands
```

*定義intents、機器人前綴字和bot*
```py
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
```

*建立bot的event偵測是否執行成功*
```py
@bot.event
async def on_ready():
    slash = await bot.tree.sync()
    print(f"登入-->{bot.user}\n載入{len(slash)}個斜線指令")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name = "上線囉!"))
```

*建立回文指令*
```py
@bot.command(name = "測試-回文指令")
async def ctx_test(ctx: commands.Context):
    await ctx.send("這是一個ctx回文指令")
```

*註冊斜線指令*
```py
@bot.tree.command(name = "測試-斜線指令-interaction")
async def slash_test_1(interaction: discord.Interaction):
    await interaction.response.send_message("這是一個interaction的斜線指令")
```

*使用TOKEN執行機器人*
```py
bot.run("TOKEN")
```


**若只是想要使用機器人可以進入我的Discord伺服器並邀請機器人:
https://discord.gg/2hMVBxuBrQ**

**小喵喵機器人邀請:
https://discord.com/oauth2/authorize?client_id=1144161789832069141**
