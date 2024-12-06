import discord, json
from discord.ext import commands
from discord.ui import Select, View

warna = 0x2C2D31
with open('./config.json') as c:
  config = json.load(c)
  ICON = config['ICON']
  PANEL_IMAGE = config['PANEL_IMAGE']
  
class BasicMC(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label="Addons", custom_id="addons1", style=discord.ButtonStyle.grey, emoji=":folde:")
    async def tutorial(self, interaction: discord.Interaction, button: discord.Button):
      embed = discord.Embed(title="", color=warna, description="""## :folder: Addons Minecraft
      
```Disini kami menawarkan addons dengan harga yang murah cuy untuk dana pelajar siap menampung```
:paket:**__Players (1 SLOT) :panah_kanan: Rp1,000__**
:paket:**__Monitoring Servers :panah_kanan: Rp25,000__**

📮Mau order bisa langsung [Pesan Sekarang](https://discord.com/channels/1268405691429949544/1268408844216959036)
      """)
      embed.set_footer(text='Please click "Dismiss Message" to clear the menu.', icon_url=ICON)
      await interaction.response.edit_message(embed=embed)
      
    @discord.ui.button(label="Back", custom_id="back1", style=discord.ButtonStyle.grey, emoji="🔙")
    async def back(self, interaction: discord.Interaction, button: discord.Button):
      embed = discord.Embed(title="",color=warna, description = """## <:minecraft:1182004196879380530>Hosting Minecraft Basic

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
      await interaction.response.edit_message(embed=embed)