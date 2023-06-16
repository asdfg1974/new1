import discord 
import os
from discord.ext import commands 

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix='$', intents=intents) 



@bot.event
async def on_ready(): 
    print(f'We have logged in as {bot.user}')


@bot.command(name = 'weather') 
async def hello(ctx): 
    await ctx.send(f'Сейчас на улице около 25 градусов ') 



@bot.command(name = 'advices') 
async def hello(ctx): 
    await ctx.send('Берегите природу!') 





















    
@bot.command(name = 'start') 
async def hello(ctx): 
    await ctx.send("""Здраствуйте, я эко-бот и я помогу вам сохранить природу! 
    Вот список моих команд: 
    animals(выдаст вам список животных, пострадавших от загрязнений)
    musor(покажет вам сколько разлагается тот или иной мусор)
    advices(даст вам советы по сохранению природы)""") 
    





@bot.command(name = 'meme')
async def meme(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command(name = 'musor')
async def meme(ctx):
    list_img = os.listdir('musor')
    for img_name in list_img:
        with open(f'musor/{img_name}', 'rb') as f:
            # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
            picture = discord.File(f)
    # Можем передавать файл как параметр!
        await ctx.send(file=picture)




@bot.command(name = 'animals')
async def meme(ctx):
    list_img = os.listdir('anym')
    for img_name in list_img:
        with open(f'anym/{img_name}', 'rb') as f:
            # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
            picture = discord.File(f)
    # Можем передавать файл как параметр!
        await ctx.send(file=picture)







@bot.command(name = 'randomanimals')
async def meme(ctx):
    list_img = os.listdir('animals111')
    img_name = random.choice(list_img)

    with open(f'animals111/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)







    
bot.run("MTEwOTExMTMxMzI5ODM2NjQ2NA.GJM2Fc.n4BveAjTzN0u9A6l4OqSGuI3KBhKKBoTlaatEw")








