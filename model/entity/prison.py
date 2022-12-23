from model.entity import *
class Prison:
    def __init__(self):
        self._prisoners = []

    def __len__(self):
        return len(self._prisoners)

    def add(self, prisoner):
        if isinstance(prisoner, Prisoner):
            self._prisoners.append(prisoner)

    def __bool__(self):
        return len(self._prisoners) != 0

    def __getitem__(self, item):
        return self._prisoners[item]

    def __setitem__(self, key, value):
        self._prisoners[key] = value

    def __delitem__(self, key):
        del self._prisoners[key]

    def __str__(self):
        if not self._prisoners:
            return f"Prison is empty"
        else:
            msg = "List of prisoners: \n"
            for prisoner in self._prisoners:
                msg += str(prisoner) + "\n"

