import discord
from subprocess import PIPE, Popen


# --- Configuration ---
token = 'ADD_YOUR_DISCORD_BOT_TOKEN_HERE'
authorized_user_id = 123456789012345678  # Replace with your Discord user ID
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
    
        print(str(message.content))
        cmdOutput = cmdline(str(message.content))
        encoding = 'utf-8'
        cmdOutput = cmdOutput.decode(encoding)
        cmdOutputBuffer = cmdOutput
        if(len(cmdOutput) > 1999):
            while(len(cmdOutputBuffer) > 1999):
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
        shell=True
    )

    return process.communicate()[0]

client.run(token)

