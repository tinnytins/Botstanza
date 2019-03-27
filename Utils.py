import csv


class Utils:
    async def handle_command(self, message):
        if message.content.startswith(';suggest'):
            self.send_suggestion(message)

    def send_suggestion(self):
        if len(message.content.split(' ')) > 1:
            sent_message = await
            client.send_message(discord.utils.get(message.server.channels, id="560207608535973888"),
                                "*" + message.author.nick + "suggested: " + message.content.split(';suggest', 1)[1])
            await
            client.add_reaction(sent_message, "\U0001F44D")
            await
            client.add_reaction(sent_message, "\U0001F44E")


class ProfanityFilter:
    words = []

    def __init__(self):
        with open('./data/BannedWords.csv', 'rt', encoding="utf8") as f:
            reader = csv.reader(f)
            for row in reader:  # each row is a list
                self.words.append(row[0])

    async def has_profanity(self, message_text):
        for word in message_text.split(' '):
            if word in self.words:
                print("gotcha")
                return True
        return False
