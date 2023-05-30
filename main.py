import discord
from discord.ext import commands

bot = commands.Bot("!")

@bot.event
async def on_ready():
    print(f"Estou pronto! Estou conectado como {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "palavrão" in message.content:
        await message.channel.send(
            f"Por favor, {message.author.name}, não ofenda os demais usuários"
        )

        await message.delete()

    await bot.process_commands(message)

@bot.command(name="oi")
async def send_hello(ctx):
    name = ctx.author.name

    response = "Olá," + name

    await ctx.send(response)


bot.run("MTExMDY0Njg2ODI1OTY1NTc0Mw.GtBvx1.DW0RCZXoQ1OPPBLD0rTT_6r8JICmtCbKL1DEGA")