from model.entity import *

class Killer(Prisoner):
    def __init__(self, name, age, term, victim=1, article=2):
        self._name = name
        self._age = age
        self._article = article
        self._term = term
        self._victim = victim

    @property
    def victim(self):
        return self._victim

    @victim.setter
    def victim(self, victim):
        if victim < 3:
            self._victim = victim


    def __str__(self):
        return (f"{self._name}, age: {self._age}, "
                f"article: {self._article}, term = {self._term}, "
                f"number of victims = {self._victim}")