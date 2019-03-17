import discord
import random
import flask
import os
from keep_alive import keep_alive
from discord.ext import commands

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_ready():
    print(f'Connected as: {bot.user.name} \nBot ID#: {bot.user.id}')

@bot.group()
async def myip(): pass

@myip.command(aliases=['Add'])
async def add():
    await bot.say("To add an IP contact @Cindy Lou Who#3346") 

@myip.command(aliases=['Help'])
async def help():
    await bot.say("Command Arguments: cindy, alvin, nick, epoodle, mps64, jddark, xen, elfman, marioluigijam")  

@myip.command(aliases=['Cindy'])
async def cindy():
    await bot.say("159.89.214.31 27786")

@myip.command(aliases=['Alvin'])
async def alvin():
    await bot.say("99.91.164.212 27886")

@myip.command(aliases=['Nick'])
async def nick():
    await bot.say("98.166.228.23 27886")

@myip.command(aliases=['EPoodle', 'Epoodle', 'ePoodle'])
async def epoodle():
    await bot.say("173.52.231.110 27886")

@myip.command(aliases=['MPS64'])
async def mps64():
    await bot.say("100.36.76.42 6407")

@myip.command(aliases=['JDDark'])
async def jddark():
    await bot.say("47.208.93.124 27999")

@myip.command(aliases=['Xen'])
async def xen():
    await bot.say("47.185.3.184 28843")

@myip.command(aliases=['Elfman', 'Elfman13', "elfman13"])
async def elfman():
    await bot.say("73.36.190.100 27886")

@myip.command(aliases=["MarioLuigiJam"])
async def marioluigijam():
    await bot.say("107.213.16.16 43000")

@bot.group()
async def party(): pass

@party.command(aliases=['4-7'])
async def fourthroughseven():
    mp4through7=['4','5','6','7']
    await bot.say(random.choice(mp4through7))

@party.command(aliases=['1-3'])
async def onethroughthree():
    mp1through3=['1','2','3']
    await bot.say(random.choice(mp1through3))

@party.command(aliases=['1-7'])
async def onethroughseven():
    mp1through7=['1','2','3','4','5','6','7']
    await bot.say(random.choice(mp1through7))

@bot.group()
async def roll(): pass

@roll.command(aliases=['2'])
async def two():
    board1list=['1','2']
    await bot.say(random.choice(board1list))

@roll.command(aliases=['3'])
async def three():
    board1list=['1','2','3']
    await bot.say(random.choice(board1list))

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
