from model.entity import *

class Thief(Prisoner):
    def __init__(self, name, age, term, article=3, death_penalty=False):
        self._name = name
        self._age = age
        self._article = article
        self._term = term
        self._death_penalty = death_penalty

        @property
        def death_penalty(self):
            return self._death_penalty

        @death_penalty.setter
        def alive(self, death_penalty):
            self._death_penalty = death_penalty


    def __str__(self):
        return (f"{self._name}, age: {self._age}, "
                f"article: {self._article}, term = {self._term},")