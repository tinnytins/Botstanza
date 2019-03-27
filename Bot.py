import discord
import time
from RPS101.RPS101 import RPS101
from Utils import ProfanityFilter


class MyClient(discord.Client):

    RPSEnabled = True
    rps = RPS101()
    ProfanityFilterEnabled = True
    ProfanityFilter = ProfanityFilter()

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        return_messages = []
        if self.ProfanityFilterEnabled:
            if await self.ProfanityFilter.has_profanity(message.content):
                await client.add_roles(message.author, discord.utils.get(message.server.roles, id="533938366044045312"))
        if message.content.startswith(';'):
            # don't respond to ourselves
            if message.author == self.user:
                return
            if self.RPSEnabled:
                return_messages.append(await MyClient.rps.handle_command(message))
            if return_messages != [None]:
                if len(return_messages) == 1:
                    await client.send_message(message.channel, return_messages[0].message_content)
                else:
                    for current_message in return_messages:
                        await client.send_message(message.channel, current_message)
                        time.sleep(3)


client = MyClient()
client.run('NDMwNzYxNTY5NTMwNDEzMDk2.D3aphw.lyFK0GGGftMvox1jriEEgJeQ0ao') 
