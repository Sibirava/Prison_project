from model.entity import *

class Converter:

    @staticmethod
    def convert_to_string(prisoners):
        s = "List of prisoners: \n"

        if not isinstance(prisoners, (list, tuple)):
            return "List is empty"

        for prisoner in prisoners:
            if isinstance(prisoner, Prisoner):
                s += "\n" + str(prisoner)

        return s