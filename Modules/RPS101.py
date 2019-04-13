import json
from Modules.RP101SupportClasses import *
from Utils import Configuration


class RPS101:
    pairings = []
    current_choices = []

    def __init__(self):
        with open("./data/pairings.json") as json_file:
            data = json.load(json_file)
            for pairing in data["pairings"]:
                self.pairings.append(Pairing(pairing["winner"], pairing["loser"], pairing["verb"]))

    async def handle_command(self, message, client):
        return_message = ""
        if message.content == "new":
            return_message = await self.begin_game()
        elif message.content == "clear":
            return_message = await self.clear_game()
        elif message.content.startswith("add"):
            return_message = await self.add_item(message.content.split("add", 1)[1].strip(), message.author)
        elif message.content == "end":
            return_message = await self.calculate_winner(client, message.channel)
        elif message.content.startswith("countdown"):
            return_message = "this is broken"
        elif message.content == "options":
            return_message += "```"
            for x in Items:
                return_message += x.name.lower().capitalize() + " = " + str(x.value) + "\n"
            return_message += "```"
        elif message.content.startswith(";whatis"):
            message_content = message.content.strip()
            if len(message_content.split(" ")) > 1:
                object_name = message_content.split(" ")[1].lower().capitalize()
                if not any(x for x in Items if x.name == object_name):
                    return_message = "Invalid object"
                else:
                    return_message = object_name + " is number " + str(Items[object_name].value)
            else:
                return_message = "Need object to assess"
        if return_message != "":
            await client.send_message(message.channel, return_message)

    async def add_item(self, add_text, adding_player):
        if add_text == "" or not any(item for item in Items if item.name.upper() == add_text.upper()):
            return "invalid add"
        else:
            self.current_choices.append(PlayerChoice(Items[add_text.lower().capitalize()], adding_player))
            return "adding " + add_text

    async def begin_game(self):
        if len(self.current_choices) > 0:
            return "There is already a game in progress, use **{0}clear** to reset it then try again".format(
                Configuration.prefix)
        else:
            return "Starting a new game of RPS101"

    async def clear_game(self):
        self.current_choices = []
        return "Current game cleared"

    async def calculate_winner(self, client, channel):
        if len(self.current_choices) < 2:
            return "Not enough entries to finish game"
        else:
            self.current_choices.sort()
            while len(self.current_choices) > 1:

                if self.current_choices[0].value + 50 > 101:
                    end_index = (self.current_choices[0].value + 50) - 101
                else:
                    end_index = self.current_choices[0].value + 50

                if end_index > self.current_choices[1].value:
                    self.current_choices.remove(1)
                    client.send_message(channel, self.get_verb_string(self.current_choices[0].value,
                                                                      self.current_choices[1].value))
                else:
                    self.current_choices.remove(0)
                    client.send_message(channel, self.get_verb_string(self.current_choices[1].value,
                                                                      self.current_choices[0].value))

    async def get_verb_string(self, winner, loser):
        verb = "this pairing is not in the list, woops"
        for pairing in self.pairings:
            if pairing.winner == winner.value and pairing.loser == loser.value:
                verb = pairing.verb
                break
        return verb
