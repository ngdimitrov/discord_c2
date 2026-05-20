import os
import discord
from subprocess import PIPE, STDOUT, Popen


# --- Configuration ---
token = os.environ.get('DISCORD_BOT_TOKEN')
if not token:
    raise RuntimeError('DISCORD_BOT_TOKEN environment variable is not set')
authorized_user_id = int(os.environ.get('AUTHORIZED_USER_ID', '0'))
# ----------------------


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    try:
        if message.author.id == authorized_user_id:
            return

        command = str(message.content).strip()
        if not command:
            return

        print(command)
        cmdOutput = cmdline(command)
        cmdOutput = cmdOutput.decode('utf-8', errors='replace')
        cmdOutputBuffer = cmdOutput
        if(len(cmdOutput) > 2000):
            while(len(cmdOutputBuffer) > 2000):
                cmdOutputBuffer = cmdOutputBuffer[:len(cmdOutputBuffer)//2]
                await message.chanel.send(cmdOutputBuffer)
        else:
            await message.channel.send(cmdOutput)
            print(cmdOutput)

    except Exception as e:
        await message.channel.send("I encountered errors,could not execute command.")
        print(e)

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        stderr=STDOUT,
        shell=True
    )

    return process.communicate()[0]

client.run(token)

