from discord.ext import commands
import os, dotenv, discord, logging, asyncio
from src import bot_class
from fixedstr import *
from config import *
from src.helpers import PermissionTier as pt, codeblock_wrap, log_exc
class AdminCommands(commands.Cog):
    def __init__(self, bot:bot_class.Bot):
        self.bot = bot
        self._logger = logging.getLogger(self.__class__.__name__)
    async def _fem(self):
        self.checkbox = await self.bot.fetch_application_emoji(1506076539073204375)
    def _log(self, msg:str):
        self._logger.info(msg)
    @commands.command(name="resync")
    async def resync(self,ctx:commands.Context):
        if not pt(ctx.author).DEV:return
        else:ctx.message.add_reaction(self.checkbox)
        self._log("Resyncing command tree with discord...")
        try:await self.bot.tree.sync()
        except Exception as e:
            self._log("Error syncing command tree:")
            log_exc(self._logger,e)
    @commands.command(name="sql")
    async def sql(self,ctx:commands.Context,query:str):
        if not pt(ctx.author).DEV:return
        else:ctx.message.add_reaction(self.checkbox)
        self._log("Executing SQL query: {}".format(query))
        try:
            await self.bot.get_cog("DatabaseModule").db.execute(query)
        except Exception as e:
            self._log("Error executing SQL query:")
            log_exc(self._logger,e)
    @commands.command(name="inline")
    async def inline(self,ctx:commands.Context,code:str):
        if not pt(ctx.author).DEV:return
        else:ctx.message.add_reaction(self.checkbox)
        self._log("Executing inline code: {}".format(code))
        try:
            exec("def __main():\n    "+code+"\n\nasyncio.create_task(__main())",globals(),locals())
        except Exception as e:
            self._log("Error executing inline code:")
            log_exc(self._logger,e)
    @commands.command(name="shutdown")
    async def shutdown(self,ctx:commands.Context):
        if not pt(ctx.author).DEV:return
        else:ctx.message.add_reaction(self.checkbox)
        self._log("Shutting down since command invoked...")
        await self.bot.close()

async def setup(bot):
    cog = AdminCommands(bot)
    await cog._fem()
    await bot.add_cog(cog)
    cog._log(load_s)
    if not CONST_DEVELOPERS_MAXPERM_DEBUG:
        cog._log("AdminCommands loaded, but not available to anyone because CONST_DEVELOPERS_MAXPERM_DEBUG is False!")

# This file is meant to be a template for new cogs. It doesn't do anything by design, only makes my life easier so i don't
# have to rewrite the same code every time i create a functionality cog.

##DEVNOTES:
## .format() and ondef type annotations are NOT used in an attempt to be
## in the very least compatible with older versions of python.
## This isn't required, and i will likely stop doing this in the future,
## but it's nice to have in case this project needs to be run on a machine supporting only older python versions.