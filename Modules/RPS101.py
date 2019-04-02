# import json
# from Modules.RP101SupportClasses import *
# class RPS101:
#     pairings = []
#     currentChoices = []
#
#     def __init__(self):
#         with open('./data/pairings.json') as json_file:
#             data = json.load(json_file)
#             for pairing in data['pairings']:
#                 self.pairings.append(Pairing(pairing['winner'], pairing['loser'], pairing['verb']))
#
#     async def handle_command(self, message):
#         if message.content == ';new':
#             return await self.begin_game()
#         elif message.content == ';clear':
#             return await self.clear_game()
#         elif message.content.startswith(';add'):
#             return await self.add_item(message.content, message.author)
#         elif message.content == ';end':
#             return await self.end_game()
#         elif message.content.startswith(';countdown'):
#             return await self.countdown()
#         elif message.content == ';options':
#             out_str = "```"
#             for x in Items:
#                 out_str += x.name.lower().capitalize() + ' = ' + str(x.value + 1) + '\n'
#             out_str += '```'
#         #  await client.send_message(message.channel, out_str)
#         elif message.content.startswith(';whatis'):
#             message_content = message.content.strip()
#             message_text = ""
#             if len(message_content.split(' ')) > 1:
#                 objectName = message_content.split(' ')[1].lower().capitalize()
#                 if not any(x for x in Items if x.name == objectName):
#                     message_text = 'Invalid object'
#                 else:
#                     message_text = objectName + ' is number ' + str(Items[objectName].value)
#             else:
#                 message_text = "Need object to assess"
#             await client.send_message(message.channel, message_text)
#
#     async def add_item(self, add_text, adding_player):
#         if add_text == '' or not any(item for item in Items if item.name == add_text.upper()):
#             return 'invalid add'
#         else:
#             self.currentChoices.append(PlayerChoice(Items[add_text.lower().capitalize()], adding_player))
#             return 'adding ' + add_text
#
#     async def begin_game(self):
#         if len(self.currentChoices) > 0:
#             return MessageObject("There is already a game in progress, use *;clear* to end it then try again", 0)
#         else:
#             return MessageObject("Starting a new game of RPS101", 0)
#
#     async def end_game(self):
#         if len(self.currentChoices) < 2:
#             return MessageObject("Not enough entries to finish game", 0)
#         else:
#             return await self.calculate_winner()
#
#     async def clear_game(self):
#         self.currentChoices = []
#         return "Current game cleared"
# #async def countdown(self):
#
# # async def calculate_winner(self):
# #     index = 0
# #     list_sorted = False
# #     while not list_sorted:
# #         list_sorted = True
# #         if object_list[index].value > object_list[index + 1].value:
# #             temp = object_list[index + 1]
# #             object_list[index + 1] = object_list[index]
# #             object_list[index] = temp
# #             list_sorted = False
# #         if index >= len(object_list) - 1:
# #             index = 0
# #     count = 0
# #     while len(object_list) > 1:
# #         return_message_text = ""
# #         beats_upto = object_list[0].value + 50
# #         if beats_upto < 100:
# #             if beats_upto > object_list[1].value:
# #                 return_message_text = "{0} beats {1}".format(object_list[0].name, object_list[1].name)
# #                 del object_list[1]
# #             else:
# #                 return_message_text = "{1} beats {0}".format(object_list[0].name, object_list[1].name)
# #                 del object_list[0]
# #         else:
# #             if beats_upto - 100 > object_list[count + 1].value:
# #                 return_message_text = "{0} beats {1}".format(object_list[0].name, object_list[1].name)
# #                 del object_list[1]
# #             else:
# #                 return_message_text = "{1} beats {0}".format(object_list[0].name, object_list[1].name)
# #                 del object_list[0]
# #         await client.send_message(output_channel, return_message_text)
# #         time.sleep(3)
# #     await client.send_message(output_channel, '{0} wins!'.format(object_list[0].name))
