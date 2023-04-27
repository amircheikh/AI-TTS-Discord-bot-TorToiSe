import discord
import random
from discord.ext import commands
import app
import io
import asyncio

intents = discord.Intents.all()
intents.members = True
intents.messages = True  # Add this line to enable the messages intent.

client = commands.Bot(command_prefix=';', intents=intents)

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def generate_tts(ctx, voice, *text):
    print ("Generating tts")
    await ctx.send("Generating your text to speech with the voice " + voice + ". This may take a while, please wait and do not send another request.") 
    text = " ".join(text)
    try:
        # Set a timeout for the app.gen function call
        filename = await asyncio.wait_for(asyncio.to_thread(app.gen, voice, text), timeout = 500)

    except asyncio.TimeoutError:
        await ctx.send("Sorry, the text to speech generation timed out. Try a shorter prompt or try again later.")

    except Exception as e:
        await ctx.send(f"Something went horribly wrong: {e}")

    with open(filename, 'rb') as f:
        wav_data = f.read()
        wav_file = io.BytesIO(wav_data) #Required for opening the WAV file
        await ctx.send(file=discord.File(wav_file, filename=filename))
        print ("Generation sent")
    


client.run("BOT TOKEN HERE")
