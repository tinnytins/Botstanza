import json
import discord
import jsonpickle

class Utils:

    async def handle_command(self, message, client):
        if message.content.startswith("report"):
            await client.send_message(discord.utils.get(
                message.server.channels, id=Configuration.report_channel), self.build_report_string(message))
        if message.content.startswith("suggest") and Configuration.suggestions_enabled:
            if message.author.nick is not None:
                name = message.author.nick
            else:
                name = message.author.name
            sent_message = await client.send_message(discord.utils.get(
                message.server.channels, id=Configuration.suggestions_channel),
                self.build_suggest_string(message))
            await client.add_reaction(sent_message, "\U0001F44D")
            await client.add_reaction(sent_message, "\U0001F44E")
        if message.content.lower().startswith("excludechannel") and message.author.server_permissions.administrator:
            Configuration.filter_excluded_channels.append(message.channel.id)
            self.save_json(Configuration.__dict__, './conf.json')
        if message.content.lower().startswith("commands"):
            await client.send_message(message.channel, self.build_command_list())

    @staticmethod
    def build_command_list():
        commands = ""
        for command in json.load(open("./data/commands.json"))["Commands"]:
            commands += "```Name: {0}\nDescription: {1}\nExample: {2}```".format(command["CommandText"], command["Description"],
                                                                         command["Example"].format(Configuration.prefix))
        return commands

    @staticmethod
    def build_suggest_string(message):
        return "*{0}* suggested: {1} ".format(message.author.mention,
                                              message.content.split("suggest",
                                                                    1)[1])

    @staticmethod
    def build_report_string(message):
        return "user *{0}* has reported user *{1}* for \"{2}\"".format(message.author.mention,
                                                                       message.content.split(" ")[1],
                                                                       message.content.split(" ", 2)[2]).strip()

    @staticmethod
    def save_json(object, path):
        with open(path, 'w') as outfile:
           outfile.write(jsonpickle.encode(object))


class Configuration(object):
    # general
    server = ""
    bot_token = ""
    staff_channel = ""
    mute_role = ""
    prefix = ""
    report_channel = ""
    selfies_channel = ""
    intro_channel = ""

    # rps
    rps_enabled = ""

    # Profanity filter
    filter_enabled = ""
    filter_words_path_severe = ""
    filter_words_path_moderate = ""
    filter_excluded_channels = []

    # suggestions
    suggestions_enabled = ""
    suggestions_channel = ""

    @staticmethod
    def __init__():
        conf = json.load(open("conf.json", "r"))
        Configuration.server = conf["server"]
        Configuration.bot_token = conf["BotToken"]
        Configuration.rps_enabled = conf["RPSEnabled"]
        Configuration.filter_enabled = conf["ProfanityFilterEnabled"]
        Configuration.filter_words_path_severe = conf["BannedWordsPathSevere"]
        Configuration.staff_channel = conf["StaffChannel"]
        Configuration.suggestions_channel = conf["SuggestionsChannel"]
        Configuration.mute_role = conf["MuteRole"]
        Configuration.filter_words_path_moderate = conf["BannedWordsPathModerate"]
        Configuration.suggestions_enabled = True
        Configuration.prefix = conf["Prefix"]
        Configuration.report_channel = conf["ReportChannel"]
        Configuration.selfies_channel = conf["SelfiesChannel"]
        Configuration.intro_channel = conf["IntroductionChannel"]
        Configuration.filter_excluded_channels = conf["FilterExcludedChannels"]
