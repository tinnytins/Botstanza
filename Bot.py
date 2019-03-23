import discord
import time
from enum import Enum
class Options(Enum):
    DYNAMITE = 0
    TORNADO = 1
    QUICKSAND = 2
    PIT = 3
    CHAIN = 4
    GUN = 5
    LAW = 6
    WHIP = 7
    SWORD = 8
    ROCK = 9
    DEATH = 10
    WALL = 11
    SUN = 12
    CAMERA = 13
    FIRE = 14
    CHAINSAW = 15  
    SCHOOL = 16
    SCISSORS = 17
    POISON = 18
    CAGE = 19
    AXE = 20
    PEACE = 21
    COMPUTER = 22
    CASTLE = 23
    SNAKE = 24
    BLOOD = 25
    PORCUPINE = 26
    VULTURE = 27
    MONKEY = 28
    KING = 29
    QUEEN = 30
    PRINCE = 31
    PRINCESS = 32
    POLICE = 33
    WOMAN = 34
    BABY = 35
    MAN = 36 
    HOME = 37
    TRAIN = 38
    CAR = 39
    NOISE = 40
    BICYCLE = 41
    TREE = 42
    TURNIP = 43
    DUCK = 44
    WOLF = 45
    CAT = 46
    BIRD = 47
    FISH = 48
    SPIDER = 49
    COCKROACH = 50
    BRAIN = 51
    COMMUNITY = 52
    CROSS = 53
    MONEY = 54
    VAMPIRE = 55
    SPONGE = 56
    CHURCH = 57
    BUTTER = 58
    BOOK = 59
    PAPER = 60
    CLOUD = 61
    AIRPLANE = 62
    MOON = 63
    GRASS = 64
    FILM = 65
    TOILET = 66
    AIR = 67 
    PLANET = 68
    GUITAR = 69
    BOWL = 70
    CUP = 71
    BEER = 72
    RAIN = 73
    WATER = 74
    TV = 75
    RAINBOW = 76
    UFO = 77
    ALIEN = 78
    PRAYER = 79
    MOUNTAIN = 80
    SATAN = 81
    DRAGON = 82
    DIAMOND = 83
    PLATINUM = 84
    GOLD = 85
    DEVIL = 86
    FENCE = 87
    VIDEOGAME = 88
    MATH = 89
    ROBOT = 90
    HEART = 91
    ELECTRICITY = 92
    LIGHTNING = 93
    MEDUSA = 94
    POWER = 95
    LASER = 96
    NUKE = 97
    SKY = 98
    TANK = 99
    HELICOPTER = 100

class MyClient(discord.Client):
    currentItems = []
    async def on_ready(self):
        print('Logged on as', self.user)

    async def calculateWinner(objectList, outputChannel):  
        index = 0
        isSorted = False
        while isSorted == False:
            isSorted = True
            if objectList[index].value > objectList[index+1].value:
                temp = objectList[index+1]
                objectList[index+1] = objectList[index]
                objectList[index] = temp
                isSorted = False
            if index >= len(objectList)-1:
                index = 0 
        count = 0
        while len(objectList) > 1:
            returnMessage = ""
            endValue = objectList[0].value+50
            if endValue < 100:
                if endValue > objectList[1].value: 
                    returnMessage = "{0} beats {1}".format(objectList[0].name, objectList[1].name)
                    del objectList[1]
                else:
                    returnMessage = "{1} beats {0}".format(objectList[0].name, objectList[1].name)
                    del objectList[0]
            else:
                if endValue-100 > objectList[count+1].value:
                    returnMessage = "{0} beats {1}".format(objectList[0].name, objectList[1].name)
                    del objectList[1]
                else:
                    returnMessage = "{1} beats {0}".format(objectList[0].name, objectList[1].name)
                    del objectList[0]
            await client.send_message(outputChannel, returnMessage)
            time.sleep(3)
    
    async def on_message(self, message):
        if message.content.startswith(';'):
            # don't respond to ourselves
            if message.author == self.user:
                return
            if message.content == ';new':
                await client.send_message(message.channel,'starting a new game of rps')
                currentItems = []
            if message.content.startswith(';add'):
                item = message.content.split(' ')[1]
                if item == ''  or not any(x for x in Options if x.name == item.upper()):
                    await client.send_message(message.channel,'invalid add')
                else:
                    await client.send_message(message.channel, 'adding '+item)
                    MyClient.currentItems.append(Options[item.upper()])
            if message.content == ';end':
                if len(MyClient.currentItems) < 2 :
                    await client.send_message(message.channel,'not enough entries')
                else:
                    await MyClient.calculateWinner(MyClient.currentItems, message.channel)
            if message.content.startswith(';countdown'):
                x = 0
                if message.content.split(' ')[1] is not None:
                    x = int(message.content.split(' ')[1])
                else:
                    x = 10
                while x > 0:
                    await client.send_message(message.channel,x)
                    x -= 1
                    time.sleep(1)
            if message.content == ';nortest':
                await client.send_message(message.channel,'disse testene gjør meg tørst')

client = MyClient()
client.run('') 
