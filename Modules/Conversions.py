import json


class Conversions:
    ConversionsList = []

    @staticmethod
    def __init__(self):
        self.ConversionsList = json.load("../data/Conversions.json")

    @staticmethod
    async def convert(message_content):
        split_values = message_content.strip().split(" ")
        first_unit = split_values[0].lower()
        second_unit = split_values[1].lower()
        value = split_values[2]

        if len(split_values) < 3 or not split_values[2].isdecimal():
            return "Invalid parameters have been provided"
        else:
            for conversion in Conversions.ConversionsList:
                if conversion.UnitA == first_unit and conversion.UnitB == second_unit:
                    return eval(conversion.AtoB.format(value))
                elif conversion.UnitB == second_unit and conversion.UnitA == first_unit:
                    return eval(conversion.BtoA.format(value))
                else:
                    return "No conversion matches the provided parameters"
   
    @staticmethod
    async def conversion_exists(unit_a,unit_b):
        for conversion in Conversions.ConversionsList:
            if conversion.UnitA == unit_a and conversion.UnitB == unit_b:
                return True
        return False
