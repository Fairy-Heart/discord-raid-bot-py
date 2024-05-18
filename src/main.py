import discord
import json
from discord.ext import commands

config_path = './config.json'

with open(config_path) as config_file:
    data = json.load(config_file)
    Token = data['TOKEN']
    Prefix = data['PREFIX']


intents = discord.Intents.default()
intents.message_content = True
intents.members = True


bot = commands.Bot(
    command_prefix = Prefix,
    intents = intents,
    case_insentive = True,
    help_command = None,
    strip_after_prefix = True
)

cogs_list = [
    'cogs.nuke',
    'cogs.events',
    'cogs.ban_all',
    'cogs.mass_kick',
    'cogs.massdm'
]


async def load_cogs():
    for cogs in cogs_list:
        try:
            await bot.load_extension(cogs)
            print('Load cogs thành công')
        except Exception as Error_On_Load_Cogs:
            print(f'Gặp lỗi khi load cogs:\n>> {Error_On_Load_Cogs}')

@bot.event
async def on_ready():
    print(f'Online thành công vào bot {bot.user}\n>> Prefix : {Prefix}')
    await bot.change_presence(
        activity = discord.Game('Huhu'),
        status = discord.Status.do_not_disturb
    )
    await load_cogs() # load cogs


bot.run(Token)