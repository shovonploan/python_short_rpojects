import discord
import youtube_dl
from discord.ext import commands
from discord.utils import get
import os
import shutil

client = commands.Bot(command_prefix=';;')


@client.event
async def on_ready():
    print('Bot is ready.')


@client.command()
async def ping(ctx):
    await ctx.send(f'ping : {round(client.latency * 1000)} ms')


@client.command(aliases=['8ball'])  # to write a function with number
async def _8ball(ctx, *, question):  # kwarg - *arg without a list
    responses = ['', '']
    await ctx.send(f'Question:{question}\nAnswer: {random.choice(responses)}')


@client.command()
async def clear(ctx, amount=6):
    await ctx.channel.purge(limit=amount)


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def unban(ctx, *, member):  # unbanning a user
    banned_users = await ctx.guild.bans()
    member_name, member_discrimimnator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discrimimnator) == (member_name, member_discrimimnator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discrimimnator}')


@client.command(pass_context=True)
async def join(ctx):
    # variable store the id of the voice channel user is on
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await ctx.send(f'Joind Voice Channel : {channel}')


@client.command(pass_context=True)
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send(f'Left Voice Channel : {channel}')
    else:
        await ctx.send(f'Bot is not currently in the Voice Channel : {channel}')

# @client.command
# async def owner(ctx):
#     user= await ctx.guild.owner
#     await ctx.send(f'{user}')

##Music Streaming Codes##


@client.command(pass_context=True)
async def play(ctx, url: str):

    voice = get(client.voice_clients, guild=ctx.guild)
    channel = ctx.message.author.voice.channel

    def check_queue():
        Queue_infile = os.path.isdir("./Queue")
        if Queue_infile is True:
            DIR = os.path.abspath(os.path.realpath("Queue"))
            length = len(os.listdir(DIR))
            still_q = length - 1
            try:
                first_file = os.listdir(DIR)[0]
            except:
                print("No more queued song(s)\n")
                queues.clear()
                return
            main_location = os.path.dirname(os.path.realpath(__file__))
            song_path = os.path.abspath(
                os.path.realpath("Queue") + "\\" + first_file)
            if length != 0:
                print("Song done, playing next queued\n")
                print(f"Songs still in queue: {still_q}")
                song_there = os.path.isfile("song.mp3")
                if song_there:
                    os.remove("song.mp3")
                shutil.move(song_path, main_location)
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, 'song.mp3')

                voice.play(discord.FFmpegPCMAudio("song.mp3"),
                           after=lambda e: check_queue())
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.07

            else:
                queues.clear()
                return

        else:
            queues.clear()
            print("No songs were queued before the ending of the last song\n")

    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            queues.clear()
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("ERROR: Music playing")
        return

    Queue_infile = os.path.isdir("./Queue")
    try:
        Queue_folder = "./Queue"
        if Queue_infile is True:
            print("Removed old Queue Folder")
            shutil.rmtree(Queue_folder)
    except:
        print("No old Queue folder")

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice.play(discord.FFmpegPCMAudio("song.mp3"),
               after=lambda e: check_queue())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit("-", 2)
    await ctx.send(f"Playing: {nname[0]}")
    print("playing\n")


@client.command(pass_context=True)
async def pause(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        voice.pause()
        await ctx.send("Music paused")
    else:
        await ctx.send("Music not playing failed pause")


@client.command(pass_context=True)
async def resume(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        voice.resume()
        await ctx.send("Resumed music")
    else:
        await ctx.send("Music is not paused")


@client.command(pass_context=True)
async def stop(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        voice.stop()
        await ctx.send("Music stopped")
    else:
        await ctx.send("No music is playing")


queues = {}


@client.command(pass_context=True)
async def queue(ctx, url: str):
    Queue_infile = os.path.isdir("./Queue")
    if Queue_infile is False:
        os.mkdir("Queue")
    DIR = os.path.abspath(os.path.realpath("Queue"))
    q_num = len(os.listdir(DIR))  # number of files in the dir
    q_num += 1
    add_queue = True
    while add_queue:
        if q_num in queues:
            q_num += 1
        else:
            add_queue = False
            # getting new queu number and updating the dictionary
            queues[q_num] = q_num

    queue_path = os.path.abspath(os.path.realpath(
        "Queue") + f"\song{q_num}.%(ext)s")  # adding the number with the song

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'outtmpl': queue_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    await ctx.send("Adding song " + str(q_num) + " to the queue")

client.run('')
