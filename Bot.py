import discord
#from Modules.RPS101 import RPS101
from WordFilter import *
from Utils import Utils
from Utils import  Configuration


class MyClient(discord.Client):
    #rps = RPS101()
    WordFilter = None
    Ready = False
    Utils = Utils()
    conf = Configuration()
    async def on_ready(self):
        print('Logged on as', self.user)
        self.WordFilter = Filter(Configuration.banned_words_path_severe,
                                 self.conf.banned_words_path_moderate)
        self.Ready = True

    async def on_message(self, message):
        if self.Ready:
            if Configuration.profanity_filter_enabled == 'True':
                await self.WordFilter.handle_command(message, self)
            if message.content.startswith(Configuration.prefix):
                message.content = message.content.strip()[1:]
                if message.author == self.user:
                    return
                #if Configuration.rps_enabled:
                   # await MyClient.rps.handle_command(message)
                await self.Utils.handle_command(message, self)
            if message.attachments and message.channel.id == Configuration.selfies_channel:
                await client.add_reaction(message, "\U00002764")


client = MyClient()
client.run('NTYxODQ5NzYxNDQ0MTM0OTM0.XKCNZA.p1WNvRVKSsvxzRmfiP67G-I5qgE')
