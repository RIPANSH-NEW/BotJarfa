import discord, json
from discord.ext import commands
from samp.basic import Basic
from samp.performance import Performance
from mc.basic import BasicMC
from discord.ui import Select, View

warna = 0x2C2D31
with open('./config.json') as c:
  config = json.load(c)
  ICON = config['ICON']
  PANEL_IMAGE = config['PANEL_IMAGE']

class Select(discord.ui.Select):
  def __init__(self):
    options=[
      discord.SelectOption(label="SA-MP Basic Cloud",emoji=":samp:",value="1",description="SA-MP AMD EPYC (Sharing)"),
      discord.SelectOption(label="SA-MP Performance Cloud",emoji=":samp:",value="2",description="SA-MP AMD RYZEN 5950X (Sharing)"),
      discord.SelectOption(label="Minecraft Basic Cloud",emoji=":minecraft:",value="3",description="MINECRAFT AMD EPYC (Sharing)"),
      discord.SelectOption(label="Bot Hosting Cloud",emoji=":discord:",value="4",description="Daftar harga hosting bot."),
      discord.SelectOption(label="Jasa SA-MP",emoji="👷",value="5",description="Jasa SA-MP list harga"),
      ]
    super().__init__(placeholder="📦 Pilih untuk melihat produk!",max_values=4,min_values=1,options=options)
  async def callback(self, interaction: discord.Interaction):
    if self.values[0] == "1":
      embed = discord.Embed(title="",color=warna, description = """## :samp:Hosting SA-MP Basic

```Basic cloud rekomendasi untuk server menengah kebawah dengan harga yang sangat murah, untuk kecepatan sangat bagus ping rendah dan sudah ada anti DDoS Basic\n\nCpu: ∞\nRam: ∞\nDisk: ∞\nBandwidth: ∞```
:paket:**__Paket#1 (25 SLOT) :panah_kanan: Rp25,000__**
:paket:**__Paket#2 (35 SLOT) :panah_kanan: Rp35,000__**
:paket:**__Paket#3 (50 + 10 SLOT) :panah_kanan: Rp50,000__**
:paket:**__Paket#4 (70 + 15 SLOT) :panah_kanan: Rp70,000__**
:paket:**__Paket#5 (100 + 25 SLOT) :panah_kanan: Rp100,000__**
:panah_bawah:
  :tambah:Include Database Online
  :tambah:Include Autobackup Setiap 1 Jam
  :tambah:Include Panel Management - untuk mengontrol server
  :tambah:Include SFTP untuk memudahkan transfer file
  :tambah:Include Anti DDoS Basic by Lost Cloud

### ‼️Information
Untuk menggunakan hosting ini anda bisa custom egg **Windows** & **Ubuntu** sesuai gamemodes anda .so atau plugin windows.

📮Mau order bisa langsung [Pesan Sekarang](https://discord.com/channels/1268405691429949544/1268408844216959036)

🎮**__Tampilan Hosting__**
      """)
      embed.set_footer(text='Please click "Dismiss Message" to clear the menu.', icon_url=ICON)
      embed.set_image(url=PANEL_IMAGE)
      await interaction.response.send_message(embed=embed, view=Basic(), ephemeral=True)
    elif self.values[0] == "2":
      embed = discord.Embed(title="",color=warna, description = """## :samp:Hosting SA-MP Performance

```Performance rekomendasi untuk server menengah keatas dengan harga yang sangat murah, untuk kecepatan sangat bagus ping rendah dan sudah ada anti DDoSv2\n\nCpu: ∞\nRam: ∞\nDisk: ∞\nBandwidth: ∞```
:paket:**__Paket#1 (50 + 5 SLOT) :panah_kanan: Rp50,000__**
:paket:**__Paket#2 (80 + 10 SLOT) :panah_kanan: Rp80,000__**
:paket:**__Paket#3 (100 + 25 SLOT) :panah_kanan: Rp120,000__**
:panah_bawah:
  :tambah:Include Bot Monitoring Servers
  :tambah:Include Database Online
  :tambah:Include Autobackup Setiap 1 Jam
  :tambah:Include Panel Management - untuk mengontrol server
  :tambah:Include SFTP untuk memudahkan transfer file
  :tambah:Include Anti DDoS Basic by XCloud

### ‼️Information
Untuk menggunakan hosting ini anda bisa custom egg **Windows** & **Ubuntu** sesuai gamemodes anda .so atau plugin windows.

📮Mau order bisa langsung [Pesan Sekarang](https://discord.com/channels/1268405691429949544/1268408844216959036)

🎮**__Tampilan Hosting__**
      """)
      embed.set_footer(text='Please click "Dismiss Message" to clear the menu.', icon_url=ICON)
      embed.set_image(url=PANEL_IMAGE)
      await interaction.response.send_message(embed=embed, view=Performance(), ephemeral=True)
    elif self.values[0] == "3":
      embed = discord.Embed(title="",color=warna, description = """## :minecraft:Hosting Minecraft Basic

```Basic cloud rekomendasi untuk server menengah kebawah dengan harga yang sangat murah, untuk kecepatan sangat bagus ping rendah dan sudah ada anti DDoS Basic\n\nCpu: ∞\nRam: ∞\nDisk: ∞\nBandwidth: ∞```
:paket:**__Paket#1 (25 SLOT) :panah_kanan: Rp35,000__**
:paket:**__Paket#2 (35 SLOT) :panah_kanan: Rp50,000__**
:paket:**__Paket#5 (80 SLOT) :panah_kanan: Rp125,000__**
:panah_bawah:
  :tambah:Include Database Online - Phpmyadmin Access
  :tambah:Include Panel Management - untuk mengontrol server
  :tambah:Include SFTP untuk memudahkan transfer file
  :tambah:Include Anti DDoS Basic by XCloud

### ‼️Information
Untuk hosting ini adalah sharing, untuk Minecraft menggunakan egg Custom

📮Mau order bisa langsung [Pesan Sekarang](https://discord.com/channels/1268405691429949544/1268408844216959036)

🎮**__Tampilan Hosting__**
      """)
      embed.set_footer(text='Please click "Dismiss Message" to clear the menu.', icon_url=ICON)
      embed.set_image(url=PANEL_IMAGE)
      await interaction.response.send_message(embed=embed, view=BasicMC(), ephemeral=True)
    elif self.values[0] == "4":
      embed = discord.Embed(title="", color=warna, description="""## 🤖Hosting Bot Cloud
      
```Kami menyediakan hosting bot untuk UCP dan untuk lainnya sebagai```
:paket:**__Harga :panah_kanan: Rp10.000__**
:panah_bawah:
  :tambah:Include Online 24/7 Jam
  :tambah:Include Support Nodejs or Python

📮Mau order bisa langsung [Pesan Sekarang](https://discord.com/channels/1268405691429949544/1268408844216959036)
      """)
      embed.set_footer(text='Please click "Dismiss Message" to clear the menu.', icon_url=ICON)
      await interaction.response.send_message(embed=embed, ephemeral=True)
    elif self.values[0] == "5":
      embed = discord.Embed(title="", color=warna, description="""## 👷Jasa SA-MP
      
```Untuk jasa SA-MP anda bisa memilih untuk jasa seperti dev, setup dll sebagainya```
:paket:**__Developer Rp150,000/Bulan__**
> By <@1125813654810534009>

:paket:**__Setup Server Rp10,000__**
> By <@1125813654810534009>

:paket:**__Fix Error Gamemodes Rp15,000__**
> By <@1125813654810534009>

:paket:**__Bot Monitoring Rp15,000__**
> By <@1125813654810534009> 

📮Mau order bisa langsung [Pesan Sekarang](https://discord.com/channels/1268405691429949544/1268408844216959036)
      """)
      embed.set_footer(text='Please click "Dismiss Message" to clear the menu.', icon_url=ICON)
      await interaction.response.send_message(embed=embed, ephemeral=True)


class SelectView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
        self.add_item(Select())