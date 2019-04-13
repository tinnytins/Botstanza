from enum import Enum
from Utils import *
import discord


class Filter:
    words_severe = []
    words_light = []

    severe_path = ""
    moderate_path = ""

    def __init__(self, severe_path, moderate_path=''):
        self.load_lists(severe_path, moderate_path)

    async def handle_command(self, message, client):
        if message.channel.id not in Configuration.filter_excluded_channels:
            if message.content.startswith('addword') and message.author.server_permissions.administrator:
                result = await self.add_word(message.content.split(' ')[1].lower())
            elif message.content.startswith('removeword') and message.author.server_permissions.administrator:
                result = await self.remove_word(message.content.split(' ')[1].lower())
            elif message.content.startswith('savewords') and message.author.server_permissions.administrator:
                result = await self.save_words()
            elif message.content.startswith('reloadlists') and message.author.server_permissions.administrator:
                result = await self.load_lists(self.severe_path, self.moderate_path)
            else:
                result = await self.has_profanity(message.content)

            if result != ProfanitySeverity.NoProfanity and result is not None:
                if result == ProfanitySeverity.Severe:
                    await client.delete_message(message)
                    await client.add_roles(message.author,
                                           discord.utils.get(message.server.roles, id=Configuration.mute_role))
                    if message.author.nick is not None:
                        name = message.author.nick
                    else:
                        name = message.author.name

                    await client.send_message(
                        discord.utils.get(message.server.channels, id=Configuration.staff_channel),
                        "Muted " + name + " for profanity, they said: ```" + message.content + "```")
                else:
                    await client.delete_message(message)
                    await client.send_message(message.channel,
                                              "https://pbs.twimg.com/media/BlbsEdPCcAANrC9.jpg")

    async def has_profanity(self, message_text):
        for word in message_text.split(' '):
            word = word.translate({ord(c): None for c in "\",.'-=+)(*&^%$£!¬`|\\?<>#~"})
            for banned_word in self.words_severe:
                if word.lower() == banned_word:
                    return ProfanitySeverity.Severe
            for banned_word in self.words_light:
                if word.lower() == banned_word:
                    return ProfanitySeverity.Moderate
        return ProfanitySeverity.NoProfanity

    async def add_word(self, word):
        if word not in self.words_severe:
            self.words_severe.append(word.lower())
        await self.save_words()

    async def remove_word(self, word):
        if word in self.words_severe:
            self.words_severe.remove(word)
        await Filter.save_words(self)

    async def save_words(self):
        await self.save_list(self.words_severe, "./data/BannedWords.csv")
        await self.save_list(self.words_light, "./data/BannedWords_Light.csv")

    async def save_list(self, list_to_save, path):
        write_str = ""
        for index in range(len(list_to_save)):
            write_str += list_to_save[index] + ","
        write_file = open(path, 'w')
        write_file.write(write_str[:-1])
        write_file.close()

    def load_lists(self, severe_path, moderate_path):
        word_file = open(severe_path, 'r')
        Filter.words_severe = word_file.read().split(',')
        word_file.close()
        if moderate_path != '':
            word_file = open(moderate_path, 'r')
            Filter.words_light = word_file.read().split(',')
            word_file.close()
        Filter.severe_path = severe_path
        Filter.moderate_path = moderate_path


class ProfanitySeverity(Enum):
    NoProfanity = 0
    Moderate = 1
    Severe = 2
