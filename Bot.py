import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.content.startswith(';'):
            # don't respond to ourselves
            if message.author == self.user:
                return
            if message.content == ';test':
                await client.send_message(message.channel, 'these tests are making me thirsty')
client = MyClient()
client.run('')
