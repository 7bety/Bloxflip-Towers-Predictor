from discord.ext import commands
import discord
import random

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is online and ready to use")

@bot.command()
async def towers(ctx, round_id):
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length < 36:
        await ctx.send("Invalid Round ID, Please Try Again.")
    elif round_length == 36:
        tower1,tower2,tower3,tower4,tower5,tower6,tower7,tower8,tower9,tower10,tower11,tower12,tower13,tower14,tower15,tower16,tower17,tower18,tower19,tower20,tower21,tower22,tower23,tower24 = "❌","❌","❌","❌","❌","❌","❌","❌","❌","❌","❌","❌","❌","❌","❌","❌","❌","❌","❌","❌","❌","❌","❌","❌"
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        c = random.randint(1, 3)
        d = random.randint(1, 3)
        e = random.randint(1, 3)
        f = random.randint(1, 3)
        g = random.randint(1, 3)
        h = random.randint(1, 3)
        if a == 1:
            tower1 == '✅'
        elif a == 2:
            tower2 = "✅"
        elif a == 3:
            tower3 = "✅"
        if b == 1:
            tower4 = "✅"
        elif b == 2:
            tower5 = "✅"
        elif b == 3:
            tower6 = "✅"
        if c == 1:
            tower7 = "✅"
        elif c == 2:
            tower8 = "✅"
        elif c == 3:
            tower9 = "✅"
        if d == 1:
            tower10 = "✅"
        elif d == 2:
            tower11 = "✅"
        elif d == 3:
            tower12 = "✅"
        if e == 1:
            tower13 = "✅"
        elif e == 2:
            tower14 = "✅"
        elif e == 3:
            tower15 = "✅"
        if f == 1:
            tower16 = "✅"
        elif f == 2: 
            tower17 = "✅"
        elif f == 3:
            tower18 = "✅"
        if g == 1:
            tower19 = "✅"
        elif g == 2:
            tower20 = "✅"
        elif g == 3:
            tower21 = "✅"
        if h == 1:
            tower22 = "✅"
        elif h == 2:
            tower23 = "✅"
        elif h == 3:
            tower24 = "✅"

        row1 = tower1 + tower2 + tower3
        row2 = tower4 + tower5 + tower6
        row3 = tower7 + tower8 + tower9
        row4 = tower10 + tower11 + tower12
        row5 = tower13 + tower14 + tower15
        row6 = tower16 + tower17 + tower18
        row7 = tower19 + tower20 + tower21
        row8 = tower22 + tower23 + tower24
        #await ctx.send(row1 + "\n" + row2 + "\n" + row3 + "\n" +row4 + "\n" +row5 + "\n" +row6 + "\n" row7 + "\n" +row8)
        info = str(random.randint(45, 95))
        pfp = 'https://c.tenor.com/rIDQGzMApaoAAAAM/black-guy.gif'
        list = [0x388519, 0x1F6104, 0x61E51F, 0x1FE57C]
        color = random.choice(list)
        em = discord.Embed(color=color)
        em.set_thumbnail(url=pfp)
        em.set_footer(text="Towers Predictor")
        em.add_field(name="made by 7bety", value=row1 + "\n" + row2 + "\n" + row3 + "\n" +row4 + "\n" +row5 + "\n" +row6 + "\n" +row7 + "\n" +row8 + "\n" + "**Accuracy**" + "\n" + info + "%")   
        await ctx.send(embed=em)



bot.run('bot token')
