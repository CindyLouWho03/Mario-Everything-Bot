import discord
import random
import os
from keep_alive import keep_alive
from discord.ext import commands

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_ready():
    print(f'Connected as: {bot.user.name} \nBot ID#: {bot.user.id}')

@bot.group()
async def board(): pass

@board.command(aliases=['1'])
async def one():
    board1list=['DKs Jungle Adventure','Peachs Birthday Cake','Yoshis Tropical Island', 'Warios Battle Canyon', 'Luigis Engine Room', 'Marios Rainbow Castle', 'Bowsers Magma Mountain', 'Eternal Star']
    await bot.say(random.choice(board1list))

@board.command(aliases=['2'])
async def two():
    board2list=['Pirate Land','Western Land','Space Land', 'Mystery Land', 'Horror Land', 'Bowser Land']
    await bot.say(random.choice(board2list))

@board.command(aliases=['3'])
async def three():
    board3list=['Chilly Waters','Deep Bloober Sea','Spiny Desert', 'Woody Woods', 'Creepy Cavern', 'Waluigis Island']
    await bot.say(random.choice(board3list))

@board.command(aliases=['4'])
async def four():
    board4list=['Toads Midway Madness','Shy Guys Jungle Jam','Goombas Greedy Gala', 'Boos Haunted Bash', 'Koopas Seaside Soiree', 'Bowser Gnarly Party']
    await bot.say(random.choice(board4list))

@board.command(aliases=['5'])
async def five():
    board5list=['Toy Dream','Rainbow Dream','Pirate Dream', 'Undersea Dream', 'Future Dream', 'Sweat Dream', 'Bowsers Nightmare']
    await bot.say(random.choice(board5list))

@board.command(aliases=['6'])
async def six():
    board6list=['Towering Treetop','E Gadds Garage','Faire Square', 'Snowflake Lake', 'Castaway Bay', 'Clockwork Castle']
    await bot.say(random.choice(board6list))

@board.command(aliases=['7'])
async def seven():
    board7list=['Grand Canal','Pagoda Peak','Pyramid Park', 'Neon Heights', 'Windmillville', 'Bowsers Enchanted Inferno']
    await bot.say(random.choice(board7list))

@board.command(aliases=['8'])
async def eight():
    board8list=['DKs Treetop Temple','Goombas Booty Boardwalk','King Boos Haunted Hideaway', 'Shy Guys Perplex Express', 'Koopas Tycoon Town', 'Bowsers Warped Orbit']
    await bot.say(random.choice(board8list))

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)
