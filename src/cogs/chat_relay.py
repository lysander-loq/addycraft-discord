from discord.ext import commands
import os, dotenv, discord, logging
from src import bot_class
from aiohttp import web
from fixedstr import *
from cnst import *
from helpers import log_exc
class AsyncHttpChatRelay(commands.Cog):
    def __init__(self, bot:bot_class.Bot):
        self.bot = bot
        self.bindport = 4577
        self._logger = logging.getLogger(self.__class__.__name__)
        self._logger
    async def notfoundfallback(self,request:web.Request):
        return web.Response(body=b"",status=404)
    async def setup(self):
        self.app = web.Application()
        self.app.router.add_post("/chat", self.chat)
        self.app.router.add_route("*", "/{tail:.*}", self.deny_all)
        self.runner = web.AppRunner(self.app)
        await self.runner.setup()
        self.site = web.TCPSite(self.runner, "127.0.0.1", self.bindport)
        await self.site.start()
    async def shutdown(self):
        if self.runner:
            await self.runner.cleanup()
            self.runner = None
            self.site = None
            self.app = None
    async def chat(self,request:web.Request):  ## WARNING: HIGHLY UNOPTIMIZED
        data = await request.json()
        try:
            assert "content" in data,"Missing content parameter in request JSON body"
            assert "srv" in data,"Missing srv parameter in request JSON body"
            assert "user" in data,"Missing user parameter in request JSON body"
            assert "staffchat" in data,"Missing staffchat parameter in request JSON body"
        except AssertionError as e:
            return web.json_response(status=400,data={"error": str(e)})
        content = data["content"]
        srv = data["srv"]
        user = data["user"]
        staffchat = data["staffchat"]
        if staffchat:return web.json_response(status=500,data={"error":PCD})
        for chid in chat_relay_channel_ids:
            ch=self.bot.get_channel(chid)
            if not ch:
                self._logger.warning("Channel with ID {} not found, skipping...".format(chid))
                continue
            wh=[i for i in await ch.webhooks()if i.name=="ChatRelayWebhook"]
            if not wh:
                self._logger.info("No webhooks found in channel #{}} ({}), creating one...".format(ch.name, ch.id))
                wh=[await ch.create_webhook(name="ChatRelayWebhook")]
            webhook=wh[0]
            try:
                content=f"**[{srv}]** {content}"
                await webhook.send(content,username=user,avatar_url="https://mc-heads.net/head/"+user+".png")
            except Exception as e:
                self._logger.error("Failed to send message to channel #{} ({}) via webhook:".format(ch.name, ch.id))
                log_exc(self._logger,e)
    def _log(self, msg:str):
        self._logger.info(msg)
    def cog_unload(self):
        self.bot.loop.create_task(self.shutdown())
async def setup(bot):
    cog = AsyncHttpChatRelay(bot)
    cog._log("Setting up AsyncHttpChatRelay...")
    await cog.setup()
    cog._log("AsyncHttpChatRelay setup finished successfully!")
    await bot.add_cog(cog)
    cog._log(load_s)