from games import tictactoe as ttt
from discord.ext import commands
from os import environ

ENV_VAR = "MAXBOTTOKEN"
TOKEN = environ.get(ENV_VAR)
COMMANDS = '''
.status: gives Max's status
.listcommands: lists all the commands available
.tictactoe: creates a new tictactoe game
'''

current_game = None
t = None

bot = commands.Bot(command_prefix=".")

@bot.command()
async def listcommands(ctx):
    await ctx.send(COMMANDS)

@bot.command()
async def status(ctx):
    await ctx.send("https://www.youtube.com/watch?v=-ZTfjUctQLM")


@bot.command()
async def tictactoe(ctx):
    global current_game, t
    current_game = "tictactoe"
    t = ttt.TicTacToe()
    await ctx.send("Use your tictactoe position like this example: L C."
                   " Where L is the respective line and C the respective column and both values are between 0 and 2. "
                   " Have fun!")
    await ctx.send(f"```{t.get_table()}```")


@bot.event
async def on_ready():
    print(f"I'm ready! {bot.user}")


@bot.event
async def on_message(msg):
    global current_game, t
    if msg.author == bot.user:
        return
    
    # tictactoe
    if current_game == "tictactoe":
        pos = msg.content.split()
        if len(pos) == 2 and pos[0].isdigit() and pos[1].isdigit():
            try:
                t.play(int(pos[0]), int(pos[1]))
            except IndexError:
                await msg.channel.send("Invalid position...\nTry again...")
            except tictactoe.PositionAlreadyOccupied:
                await msg.channel.send("Position already occupied...\nTry again...")
            await msg.channel.send(f"```{t.get_table()}```")
        result = t.won()
        if tictactoe is not None and result != -1:
            t = None
            current_game = None
            if result == 0:
                await msg.channel.send("X player won!!!")
            else:
                await msg.channel.send("O player won!!!")

    await bot.process_commands(msg)

bot.run(TOKEN)
