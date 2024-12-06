import discord, json
from discord.ext import commands
from discord.ui import Select, View

warna = 0x2C2D31
with open('./config.json') as c:
  config = json.load(c)
  ICON = config['ICON']
  PANEL_IMAGE = config['PANEL_IMAGE']

class Basic(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label="Addons", custom_id="addons1", style=discord.ButtonStyle.grey, emoji=":folder:")
    async def tutorial(self, interaction: discord.Interaction, button: discord.Button):
      embed = discord.Embed(title="", color=warna, description="""## :folder: Addons SA-MP Cloud
      
```Disini kami menawarkan addons dengan harga yang murah cuy untuk dana pelajar siap menampung```
:paket:**__Players (1 SLOT) :panah_kanan: Rp1,000__**
:paket:**__Port Voice :panah_kanan: Rp5,000__**
:paket:**__Custom Port :panah_kanan: Rp15,000__**
:paket:**__Monitoring Servers :panah_kanan: Rp10,000__**

📮Mau order bisa langsung [Pesan Sekarang](https://discord.com/channels/1268405691429949544/1268408844216959036)
      """)
      embed.set_footer(text='Please click "Dismiss Message" to clear the menu.', icon_url=ICON)
      await interaction.response.edit_message(embed=embed)
      
    @discord.ui.button(label="System Backup", custom_id="backup1", style=discord.ButtonStyle.grey, emoji="💾")
    async def backup(self, interaction: discord.Interaction, button: discord.Button):
      embed = discord.Embed(title="", color=warna, description="""## 💾 System Autobackup
      
> Jangan khawatir Lost Cloud sudah ada Autobackup menggunakan **__Google Drive__** dan dilakukan backup setiap 1 Jam sekali untuk menjaga database server **__Database.sql__** pada Phpmyadmin tetap aman.
> Kami menawarkan Autobackup dengan free setiap paket cloud

**__Tampilan Autobackup__**
      """)
      embed.set_footer(text='Please click "Dismiss Message" to clear the menu.', icon_url=ICON)
      embed.set_image(url="https://media.discordapp.net/attachments/1173697971997659196/1176984526816280608/image0.jpg?ex=6570db42&is=655e6642&hm=1db38168864560e5fea69b5501e79e09319f55481c8bea0cd76103d0f8fff0d7&")
      await interaction.response.edit_message(embed=embed)
      
    @discord.ui.button(label="Back", custom_id="back1", style=discord.ButtonStyle.grey, emoji="🔙")
    async def back(self, interaction: discord.Interaction, button: discord.Button):
      embed = discord.Embed(title="",color=warna, description = """## :samp: Hosting SA-MP Basic

```Basic cloud rekomendasi untuk server menengah kebawah dengan harga yang sangat murah, untuk kecepatan sangat bagus ping rendah dan sudah ada anti DDoS Basic\n\nCpu: ∞\nRam: ∞\nDisk: ∞\nBandwidth: ∞```
:paket:**__Paket#1 (25 SLOT) :panah_kanan: Rp25,000__**
:paket:**__Paket#2 (35 SLOT) :panah_kanan: Rp35,000__**
:paket:**__Paket#3 (50 + 10 SLOT) :panah_kanan: Rp50,000__**
:paket:**__Paket#4 (70 + 15 SLOT) :panah_kanan: Rp70,000__**
:paket:**__Paket#5 (100 + 25 SLOT) :panah_kanan: Rp100,000__**
<:apalah:1179761511367975023>
  :tambah:Include Database Online - Phpmyadmin Access
  :tambah:Include Autobackup - Setiap 1 Jam Sql
  :tambah:Include Panel Management - untuk mengontrol server
  :tambah:Include SFTP untuk memudahkan transfer file
  :tambah:Include Anti DDoS Basic by XCloud

### ‼️Information
Untuk menggunakan hosting ini anda bisa custom egg **Windows**&**Ubuntu** sesuai gamemodes anda .so atau plugin windows.

📮Mau order bisa langsung [Pesan Sekarang](https://discord.com/channels/1268405691429949544/1268408844216959036)

🎮**__Tampilan Hosting__**
      """)
      embed.set_footer(text='Please click "Dismiss Message" to clear the menu.', icon_url=ICON)
      embed.set_image(url=PANEL_IMAGE)
      await interaction.response.edit_message(embed=embed)