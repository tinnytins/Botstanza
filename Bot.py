import discord
from Modules.RPS101 import RPS101
from Modules.WordFilter import Filter
from Utils import Utils, Configuration
from Modules.Conversions import Conversions


class MyClient(discord.Client):
    rps = RPS101()
    WordFilter = None
    Ready = False
    Utils = Utils()
    conf = Configuration()

    async def on_ready(self):
        print('Logged on as', self.user)
        self.WordFilter = Filter(Configuration.filter_words_path_severe,
                                 self.conf.filter_words_path_moderate)
        self.Ready = True

    async def on_message(self, message):
        if self.Ready and message.author != self.user:
            if Configuration.filter_enabled == 'True':
                await self.WordFilter.handle_command(message, self)
            if message.content.startswith(Configuration.prefix):
                message.content = message.content.strip()[1:]
                if Configuration.rps_enabled:
                    await MyClient.rps.handle_command(message, self)
                await self.Utils.handle_command(message, self)
                if message.content.startswith("convert"):
                    await client.send_message(message.channel,
                                              await Conversions.convert(message.content.split("convert", 1)[1]))
            if message.attachments and message.channel.id == Configuration.selfies_channel:
                await client.add_reaction(message, "\U00002764")
            if message.channel.id == Configuration.intro_channel:
                await client.add_reaction(message, "\U0001F44B")


client = MyClient()
client.run(Configuration.bot_token)
