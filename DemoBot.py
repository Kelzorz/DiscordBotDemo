import discord

TOKEN = ''
MASTERS = [''] #define self

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        # await client.send_message(message.channel, msg)
        await message.channel.send(msg)
        return

    if message.content.startswith("!messagedump"):
        await messagedumpCommand(message)

    if message.content.startswith("!whoami"):
        await whoamiCommand(message)

    if message.content.startswith("!die"):
        await dieCommand(message)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_error(event, *args, **kwargs):
    return

async def messagedumpCommand(message):
    await message.channel.send(message)

async def whoamiCommand(message):
    await message.channel.send(message.author)
    await message.channel.send(message.author.id)
    await message.channel.send(message.author.status)
    if message.author.nick is not None:
        await message.channel.send(message.author.nick)
    if message.author.roles is not None:
        await message.channel.send(message.author.roles)
    if message.author.top_role is not None:
        await message.channel.send(message.author.server_permissions)

async def dieCommand(message):
    if str(message.author.id) in MASTERS:
        await message.channel.send("I think I'll kill myself...")
        exit()
    else:
        await message.channel.send("no u")

client.run(TOKEN)
