import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import requests
from ollamafreeapi import OllamaFreeAPI


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f"im ready! - {bot.user.name}")

@bot.command()
async def normalrps(ctx, *, msg):
    import random
    valid_answers = ["rock", "paper", "scissors"]
    myanswer = random.choice(valid_answers)
    if not msg.lower() in valid_answers:
        await ctx.reply("dont cheat bro")
    else:
        if msg.lower() == myanswer:
            await ctx.reply(f"i choose {myanswer}, you choose {msg.lower()} and- aw man its a tie")
        elif (msg.lower() == "rock" and myanswer == "scissors") or \
            (msg.lower() == "scissors" and myanswer == "paper") or \
            (msg.lower() == "paper" and myanswer == "rock"):
            await ctx.reply(f"i choose {myanswer}, you choose {msg.lower()} and you win :sob:")
        else:
            await ctx.reply(f"i choose {myanswer}, you choose {msg.lower()} and i win lol ez")

@bot.command()
async def fairrps(ctx, *, msg):
    await ctx.send("*Thinking without knowing your response*")
    from ollamafreeapi import OllamaFreeAPI
    client = OllamaFreeAPI()
    ans1 = msg

    response = client.chat(
    model="gpt-oss:20b",
    prompt=f"Imagine that we are playing \'Rock, Paper, Scissors\' but you can choose anything you want. Choose an object that you think would beat most things. Reply only with your answer, no explanations",
    temperature=0.7
    )

    print(response)

    response2 = client.chat(
        model="gpt-oss:20b",
        prompt=f"Does a {response} beat {ans1}? Reply \'1\' if it does, else reply \'0\'.",
        temperature=0.7
    )

    answer = int(response2)
    print(answer)
    if answer == 1:
        await ctx.reply(f"I choose {response} and win! haha.")
        await ctx.send("-# The answer was chosen by an AI")
    elif answer == 0:
            await ctx.reply(f"i choose {response} and somehow losed. UNFAIRRRR")
            await ctx.send("-# The answer was chosen by an AI")



@bot.command()
async def unfairrps(ctx, *, msg):
    await ctx.send(f"*Let me think what would beat {msg}...*")
    from ollamafreeapi import OllamaFreeAPI
    client = OllamaFreeAPI()
    ans1 = msg

    response = client.chat(
        model="gpt-oss:20b",
        prompt=f"What does beat a {ans1}? Return just one object. Only return the answer, no explanation.",
        temperature=0.7
    )

    print(response)

    response2 = client.chat(
        model="gpt-oss:20b",
        prompt=f"Does a {response} beat {ans1}? Reply \'1\' if it does, else reply \'0\'.",
        temperature=0.7
    )

    answer = int(response2)
    print(answer)
    if answer == 1:
        await ctx.reply(f"I choose {response} and win! haha.")
        await ctx.send("-# The answer was chosen by an AI")
    elif answer == 0:
            await ctx.reply(f"i choose {response} and somehow losed. UNFAIRRRR")
            await ctx.send("-# The answer was chosen by an AI")

@bot.command()
async def secret(ctx):
    from ollamafreeapi import OllamaFreeAPI
    client = OllamaFreeAPI()
    await ctx.send("*Creating a super cool message for u*")
    response = client.chat(
        model="gpt-oss:20b",
        prompt=f"Create a short message congratulating the user for founding a secret command, less than 500 characters. Reply with the first option.",
        temperature=0.7
    )

    await ctx.reply(response)

@bot.command()
async def secret2(ctx):
     await ctx.reply("## no cool ai message for u")

@bot.command()
async def cmds(ctx):
     await ctx.reply("ok theres uhh: 1. /normalrps (BORINGG) 2. /unfairrps (So you choose things like nuclear bomb) 3. /fairrps (So you choose normal things like Diamond) 4. *Secret Command* 5. *Secret Command 2*")
     

bot.run(token, log_handler=handler, log_level=logging.DEBUG)