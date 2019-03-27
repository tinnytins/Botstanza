import json


class Support:

    @staticmethod
    async def get_param(self, command, param_index):
        return command.shave.split(' ')[param_index]

    @staticmethod
    async def check_params(self,command,param_count):
        if command.shave.split(' ') != param_count:
            return False
        return True


class MessageObject:
    message_content = ""
    delay_for = 0

    def __init__(self, message_content, delay_for):
        self.message_content = message_content
        self.delay_for = delay_for
