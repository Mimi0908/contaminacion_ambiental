import discord
from discord.ext import commands
import random
import os
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}! Te ayudare a resolver todas las dudas que tengas mediante la contaminación (----) y el como solucionarlas o evitarlas de la mejor manera')

@bot.command()
async def imagen(ctx):
    img_name = random.choice(os.listdir('contaminacion_imagenes'))
    
    with open(f'contaminacion_imagenes/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

@bot.command()
async def opciones(ctx):
    await ctx.send(f'Te tengo 4 opciones que te pueden ayudar :D, selecciona la opcion colocando $ y poniendo opcion y el número de tu eleccion')

@bot.command()
async def opcion1(ctx):
    await ctx.send(f'Ahorrar agua\nToma duchas en lugar de baños, cierra los grifos cuando no los uses, riega el jardín antes de que salga el sol o después de que se haya puesto, y verifica las llaves y tuberías regularmente para encontrar fugas.')

@bot.command()
async def opcion2(ctx):
    await ctx.send(f'Usar menos agua\nUsa un vaso para enjuagarte la boca cuando te cepillas los dientes, llena un balde en lugar de una manguera para lavar el auto o la vereda, y cierra la canilla mientras enjabonas los platos y cubiertos.')

@bot.command()
async def opcion3(ctx):
    await ctx.send(f'Usar productos de limpieza sostenibles\nUsa productos de limpieza biodegradables y productos que no requieren enjuague.')

@bot.command()
async def opcion4(ctx):
    await ctx.send(f'Lavar la ropa de manera eficiente\nUsa ciclos cortos de lavado y poné el lavarropas solo cuando esté lleno.')


bot.run("token")