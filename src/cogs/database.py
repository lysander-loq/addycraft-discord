from discord.ext import commands
import os, dotenv, discord, logging, asyncpg
from src import bot_class
from fixedstr import *
class Database(commands.Cog):
    def __init__(self, bot:bot_class.Bot):
        self.bot = bot
        self._logger = logging.getLogger(self.__class__.__name__)
        os.makedirs("/data/",exist_ok=True)
        
    def _log(self, msg:str):
        self._logger.info(msg)

async def setup(bot):
    cog = Database(bot)
    await bot.add_cog(cog)
    cog._log(load_s)


##DEVNOTES:
## .format() and ondef type annotations are NOT used in an attempt to be
## in the very least compatible with older versions of python.
## This isn't required, and i will likely stop doing this in the future,
## but it's nice to have in case this project needs to be run on a machine supporting only older python versions.