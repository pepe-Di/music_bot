import discord
import asyncio
from discord.ext import commands
import youtube_dl
import random
client = commands.Bot(command_prefix="!")
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
players = {}
queues = {}


@client.command(name='join', aliases=['j', 'сюда'])
async def join(ctx):
    try:
        await ctx.author.voice.channel.connect()
    except Exception as e:
        await ctx.send("fucc you <:gnomed:875359595529388062>")


async def play_next():
     print('hello')
     await asyncio.sleep(1)
     print('world')


@client.command(name='play', aliases=['p', 'быра'])
async def play(ctx, url: str):
    try:
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        ydl_opts = {'format': 'bestaudio'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            URL = info['formats'][0]['url']
        voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    except Exception as e:
        await ctx.send("fucc you <:gnomed:875359595529388062>")


@client.command(name='leave', aliases=['l', 'нах'])
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    try:
        if voice.is_connected():
            await voice.disconnect()
    except Exception as e:
        await ctx.send("fucc you <:gnomed:875359595529388062>")


@client.command(name='pause', aliases=['ps', 'тиха'])
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("fucc you <:gnomed:875359595529388062>")


@client.command(name='resume', aliases=['r', 'дальше'])
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("fucc you <:gnomed:875359595529388062>")


@client.command(name='stop', aliases=['s', 'стоп'])
async def stop(ctx):
    try:
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        voice.stop()
    except Exception as e:
        await ctx.send("fucc you <:gnomed:875359595529388062>")


@client.command(name='pp', aliases=['пп'])
async def pp(ctx):
    username = ctx.message.author.name
    await ctx.send(str(username) + " has " + str(random.randint(0, 100)) + " pp")


class switch(object):
    def __init__(self, value):
        self.value = value  # значение, которое будем искать
        self.fall = False   # для пустых case блоков

    def __iter__(self):     # для использования в цикле for
        """ Возвращает один раз метод match и завершается """
        yield self.match
        raise StopIteration

    def match(self, *args):
        """ Указывает, нужно ли заходить в тестовый вариант """
        if self.fall or not args:
            # пустой список аргументов означает последний блок case
            # fall означает, что ранее сработало условие и нужно заходить
            #   в каждый case до первого break
            return True
        elif self.value in args:
            self.fall = True
            return True
        return False


@client.command()
async def rnd(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    try:
        for case in switch(random.randint(1, 4)):
            if case(1):
                voice.play(discord.FFmpegPCMAudio('https://cdn.discordapp.com/attachments/889565334430941275/889565371462459442/-__.mp3', **FFMPEG_OPTIONS))
                break
            if case(2):
                voice.play(discord.FFmpegPCMAudio('https://cdn.discordapp.com/attachments/889565334430941275/889565397144191046/-___JesusAVGN_.mp3', **FFMPEG_OPTIONS))
                break
            if case(3):
                voice.play(discord.FFmpegPCMAudio('https://cdn.discordapp.com/attachments/889565334430941275/889572687846989854/d191644b6b6334c2.mp3',**FFMPEG_OPTIONS))
                break
            if case(4):
                voice.play(discord.FFmpegPCMAudio('https://cdn.discordapp.com/attachments/875354204070379523/889556057897177088/audio.mp3',**FFMPEG_OPTIONS))
                break
    except Exception as e:
        await ctx.send("fucc you <:gnomed:875359595529388062>")


@client.command()
async def sound(ctx, url : str):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    try:
        voice.play(discord.FFmpegPCMAudio(url, **FFMPEG_OPTIONS))
    except Exception as e:
        await ctx.send("fucc you <:gnomed:875359595529388062>")


#@client.event
#async def on_message(message):
#    message.content = message.content.lower()
#    if message.author == client.user:
#        return
#    if message.content.startswith("<:moairev:875357014350512168"):
#        await message.channel.send("<:moai:875355368623046667>")

client.run('///')
