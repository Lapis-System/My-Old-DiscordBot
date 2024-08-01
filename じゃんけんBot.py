import discord
import random
from discord.ext import commands

# 使用する単語のリストを作成する
word_list = ['グー', 'チョキ', 'パー']

# Botのクライアントを作成する

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name}がログインしました！')

@bot.event
async def on_message(message):
    # 自分自身のメッセージには反応しないようにする
    if message.author == bot.user:
        return

    # 特定のメッセージが来たら反応する
    if message.content == 'じゃんけん':
        # 4つの単語をランダムに選ぶ
        words = random.choice(word_list)
        # 選ばれた単語をスペースで結合して送信する
        await message.channel.send(' '.join(words))


bot.run('TOKEN')
