import json
import discord


class Utils:

    async def handle_command(self, message, client):
        if message.content.startswith("report"):
            await client.send_message(discord.utils.get(
                                        message.server.channels, id=Configuration.report_channel),
                                            "user *{0}* has reported user *{1}* for \"{2}\""
                                            .format(message.author.nick,
                                            message.content.split(" ")[1],
                                            message.content.split(" ", 2)[2]).strip())
        if message.content.startswith("suggest") and Configuration.suggestions_enabled:
            sent_message = await client.send_message(discord.utils.get(
                                                      message.server.channels, id=Configuration.suggestions_channel),
                                                      "*{0}* suggested: {1} ".format(message.author.nick,
                                                                                   message.content.split("suggest",
                                                                                                         1)[1]))
            await client.add_reaction(sent_message, "\U0001F44D")
            await client.add_reaction(sent_message, "\U0001F44E")
        if message.content.startswith("convert"):
            await client.send_message(message.channel, await self.convert(message.content.split("convert", 1)[1]))

    @staticmethod
    async def convert(message_content):

        list_of_units = ("f", "c", "ft", "cm")

        split_values = message_content.strip().split(" ")
        first_unit = split_values[0].lower()
        second_unit = split_values[1].lower()

        if first_unit not in list_of_units or second_unit not in list_of_units \
                or len(split_values) < 3 or not split_values[2].isnumeric():
            return "invalid params"
        elif first_unit == "f" and second_unit == "c":
            return str(round((int(split_values[2])-32)*(5/9), 2)) + second_unit
        elif first_unit == "c" and second_unit == "f":
            return str(round(int(split_values[2])*(9/5)+32, 2)) + second_unit
        elif first_unit == "ft" and second_unit == "cm":
            return str(round(int(split_values[2])*30, 2)) + second_unit
        elif first_unit == "cm" and second_unit == "ft":
            return str(round(int(split_values[2])/30, 2)) + second_unit


class Configuration:

    # general
    bot_token = ""
    staff_channel = ""
    mute_role = ""
    prefix = ""
    report_channel = ""
    selfies_channel = ""

    # rps
    rps_enabled = False

    # Profanity filter
    profanity_filter_enabled = False
    banned_words_path_severe = ""
    banned_words_path_moderate = ""

    # suggestions
    suggestions_enabled = False
    suggestions_channel = ""

    @staticmethod
    def __init__():
        conf = json.load(open("conf.json", "r"))
        Configuration.bot_token = conf["BotToken"]
        Configuration.rps_enabled = conf["RPSEnabled"]
        Configuration.profanity_filter_enabled = conf["ProfanityFilterEnabled"]
        Configuration.banned_words_path_severe = conf["BannedWordsPathSevere"]
        Configuration.staff_channel = conf["StaffChannel"]
        Configuration.suggestions_channel = conf["SuggestionsChannel"]
        Configuration.mute_role = conf["MuteRole"]
        Configuration.banned_words_path_moderate = conf["BannedWordsPathModerate"]
        Configuration.suggestions_enabled = True
        Configuration.prefix = conf["Prefix"]
        Configuration.report_channel = conf["ReportChannel"]
        Configuration.selfies_channel = conf["SelfiesChannel"]