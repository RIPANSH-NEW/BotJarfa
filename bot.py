import discord, json
from discord.ext import commands, tasks
from handle.menu import SelectView
from discord import app_commands
from discord.ext.commands import has_permissions
from discord.ui import View
from itertools import cycle


with open('./config.json') as c:
  conf = json.load(c)
  ICON = conf['ICON']
  TOKEN = conf['TOKEN']
  PANEL_IMAGE = conf['PANEL_IMAGE']
  
CLOUD = "https://cdn.discordapp.com/attachments/1314100337682022462/1314405113045061792/20241206_083610.jpg?ex=6753a6a7&is=67525527&hm=3fc62629fcc580d10b7fdbe40ab7f750cadbfe80b762b85b1c2c4cd6e449d94a&"
intents = discord.Intents().all()
bot = commands.Bot(command_prefix="Xx",intents=intents)
WARNA = 0x2C2D31

status = cycle(["👷 Helper Jarfa",
                "🔋 Uptime 61%",
                "🛠 Created By RiPanSH"])

try:
    with open('db.json', 'r') as file:
        config = json.load(file)
except FileNotFoundError:
    config = {}
    
async def save_config():
    with open('db.json', 'w') as file:
        json.dump(config, file, indent=2)
        
@bot.event
async def on_ready():
    change_status.start()
    await bot.tree.sync()
    print(f'Logged in as {bot.user.name}')

@tasks.loop(seconds=5)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

class Buttons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label="Support", custom_id="s1", style=discord.ButtonStyle.grey, emoji=":jarfacloud:")
    async def tutorial(self, interaction: discord.Interaction, button: discord.Button):
      embed = discord.Embed(title="", color=WARNA, description="""## Support Team
> Admin akan selalu membantu jika ada yang mau ditanyakan anda hanya perlu open ticket untuk bertanya bisa jika pm Jxdn.

❗Untuk Gamemode SA-MP Support All
- plugins .so atau tidak .so
kami akan sedia EGG Windows dan Ubuntu

      """, timestamp=interaction.message.created_at)
      member = interaction.user
      embed.set_footer(text=member.name, icon_url=member.avatar)
      await interaction.response.send_message(embed=embed, ephemeral=True)
      
@bot.tree.command(name="payment",description="Payment by RiPanSH")
@commands.has_permissions(administrator=True)
async def payment(interaction:discord.Interaction):
  if not interaction.user.guild_permissions.administrator:
    return await interaction.response.send_message("Anda tidak bisa menggunakan command ini karena anda bukan administrator.", ephemeral=True)
    
  embed = discord.Embed(title="", color=WARNA, description="""## 💳**__Payment__**:jarfacloud:
Mohon ketika akan melalukan transaksi hubungi admin terlebih dahulu.
~~----------------------------------------------------------~~
>>> **:dana:Dana : 082116360676**
**:gopay:Gopay : 083891162997**
**:ovo:OVO : 082249354302**
**Qris**
  """)
  embed.set_image(url="https://cdn.discordapp.com/attachments/1173697971997659196/1181649548813271130/QrisA.png?ex=6581d3e6&is=656f5ee6&hm=2f1d02839412ed61f48488a7104e90b2406b379257b261a992733cc8c69a5c84&")
  embed.set_thumbnail(url=ICON)
  embed.set_footer(text="Jarfa Cloud // Payment", icon_url=ICON)
  await interaction.response.send_message(embed=embed)

    
@bot.tree.command(name="testimoni",description="Testimoni by RiPanSH")
@commands.has_permissions(administrator=True)
async def testimoni(interaction:discord.Interaction, buyer: discord.Member, number: int, product: discord.TextChannel, price: int, note: str, image: discord.Attachment):
  if not interaction.user.guild_permissions.administrator:
    return await interaction.response.send_message("Anda tidak bisa menggunakan command ini karena anda bukan administrator.", ephemeral=True)
  global config
  guild_id = interaction.guild.id
  guild_config = config.setdefault(str(guild_id), {})
  testimoni = guild_config.get('testimoni', None)
  if interaction.channel.id == testimoni:
      embed = discord.Embed(title="", color=WARNA, description=f"## 💼**__Testimoni #{number} <:lostcloud:1181609785678893158>__**")
      embed.add_field(name="Buyers", value=f"> {buyer.mention}")
      embed.add_field(name="Product", value=f"> {product.mention}")
      embed.add_field(name="Harga", value=f"> Rp{price:,}")
      embed.add_field(name="Note", value=f"> {note}")
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1173697971997659196/1180203979691528292/1160907935619239956.png?ex=657c919b&is=656a1c9b&hm=53388430ebff89c9f4994df443d1284baf419d8a2239835d457fac2b23220690&")
      embed.set_image(url=image.url)
      member = interaction.user
      embed.set_footer(text=member.name, icon_url=member.avatar)
      await interaction.response.send_message(embed=embed)
  else:
      await interaction.response.send_message(f"Anda tidak bisa menggunakanya disini. Only <#{testimoni}>", ephemeral=True)

@bot.tree.command(name="feedback",description="Feedback by RiPanSH")
@app_commands.choices(rate=[
    discord.app_commands.Choice(name="⭐", value="⭐"),
    discord.app_commands.Choice(name="⭐⭐", value="⭐⭐"),
    discord.app_commands.Choice(name="⭐⭐⭐", value="⭐⭐⭐"),
    discord.app_commands.Choice(name="⭐⭐⭐⭐", value="⭐⭐⭐⭐"),
    discord.app_commands.Choice(name="⭐⭐⭐⭐⭐", value="⭐⭐⭐⭐⭐"),
        ])
async def feedback(interaction:discord.Interaction, seller: discord.Member, rate: discord.app_commands.Choice[str], ulasan: str):
  global config
  guild_id = interaction.guild.id
  guild_config = config.setdefault(str(guild_id), {})
  feed_back = guild_config.get('feedback')
  if interaction.channel.id == feed_back:
    embed = discord.Embed(title="", color=WARNA, description="## 📝 **__Feedback__** :jarfacloud:\n\nTerimakasih telah membeli produk kami, kami akan berusaha semaksimal mungkin untuk menjadi yang terbaik.")
    embed.add_field(name="Nama Seller",value=f"> {seller.mention}")
    embed.add_field(name="Rating", value=f"> {rate.value}")
    embed.add_field(name="Ulasan", value=f"> {ulasan}")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1314100337682022462/1314405113045061792/20241206_083610.jpg?ex=6753a6a7&is=67525527&hm=3fc62629fcc580d10b7fdbe40ab7f750cadbfe80b762b85b1c2c4cd6e449d94a&")
    embed.set_image(url=CLOUD)
    member = interaction.user
    embed.set_footer(text=member.name, icon_url=member.avatar)
    await interaction.response.send_message(embed=embed)
  else:
    await interaction.response.send_message(f"Anda tidak bisa menggunakanya disini. Only <#{feed_back}>", ephemeral=True)
    
@bot.tree.command(name="setestimoni",description="Setestimoni by RiPanSH")
@commands.has_permissions(administrator=True)
async def setestimoni(interaction:discord.Interaction, channel: discord.TextChannel):
  if not interaction.user.guild_permissions.administrator:
    return await interaction.response.send_message("Anda tidak bisa menggunakan command ini karena anda bukan administrator.", ephemeral=True)
  global config
  guild_config = config.setdefault(str(interaction.guild.id), {})
  guild_config['testimoni'] = channel.id
  await save_config()
  await interaction.response.send_message(f"Testimoni berhasil di setting di channel {channel.mention}", ephemeral=True)
  
@bot.tree.command(name="setfeedback",description="Setfeedback by RiPanSH")
@commands.has_permissions(administrator=True)
async def setfeedback(interaction:discord.Interaction, channel: discord.TextChannel):
  if not interaction.user.guild_permissions.administrator:
    return await interaction.response.send_message("Anda tidak bisa menggunakan command ini karena anda bukan administrator.", ephemeral=True)
  global config
  guild_config = config.setdefault(str(interaction.guild.id), {})
  guild_config['feedback'] = channel.id
  await save_config()
  await interaction.response.send_message(f"Feedback berhasil di setting di channel {channel.mention}", ephemeral=True)

@bot.tree.command(name="menu",description="Menu product by jarfa Cloud")
@commands.has_permissions(administrator=True)
async def menu(interaction:discord.Interaction):
  if not interaction.user.guild_permissions.administrator:
    return await interaction.response.send_message("Anda tidak bisa menggunakan command ini karena anda bukan administrator.", ephemeral=True)
  embed = discord.Embed(title="",  color=WARNA,
  description="""##  <:informasi:1181621768646053969>Lost Cloud Product<:lostcloud:1181609785678893158>

Disini tempat untuk mencari product hosting dan dll, Daftar menu ada disini bisa anda pilih salah satu dari berbagai produk cuy.
  """)
  embed.set_footer(text='Jarfa Cloud Hosting Game', icon_url=ICON)
  embed.set_image(url="https://cdn.discordapp.com/attachments/1314100337682022462/1314405113045061792/20241206_083610.jpg?ex=6753a6a7&is=67525527&hm=3fc62629fcc580d10b7fdbe40ab7f750cadbfe80b762b85b1c2c4cd6e449d94a&")
  await interaction.response.send_message(embed=embed, view=SelectView())
  await interaction.response.send_message(view=Buttons())

async def on_message(message):
  if message.content.startswith('<@1135197516879634484>'):
    embed = discord.Embed(title="", description="""## **__<:jarfacloud:Jarfa Cloud__**
>>> Mohon tunggu ya mungkin Ripanz sedang off/sibuk, jika online selalu fash respons.
    """,color=WARNA)
    await message.channel.send(embed=embed)
    
async def on_member_join(member):
    welcome_channel = bot.get_channel(1268441919688671262)
    if welcome_channel:
        await welcome_channel.send(f"""Selamat datang di :jarfacloud:**__Jarfa Cloud && RiPanSH Community__** 👋🎮!!{member.mention} 
>>> Jarfa Cloud bukan sekadar penyedia layanan hosting biasa. Kami berkomitmen untuk memberikan pengalaman gaming terbaik, menghadirkan performa yang unggul, kestabilan server, dan dukungan teknis yang responsif. Kami memahami bahwa kepuasan Anda adalah prioritas utama kami.""")
    else:
        print("Channel welcome tidak ditemukan.")
        
bot.event(on_message)
bot.event(on_member_join)
bot.run(TOKEN)