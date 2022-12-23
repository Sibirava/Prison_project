from model.entity import *

class SerialKiller(Killer):
    def __init__(self, name, age, term, victim, death_penalty=True, article=3):
        self._name = name
        self._age = age
        self._article = article
        self._term = term
        self._death_penalty = death_penalty
        self._victim = victim

    @property
    def death_penalty(self):
        return self._death_penalty

    @death_penalty.setter
    def death_penalty(self, death_penalty):
        self._death_penalty = death_penalty

    def __str__(self):
        return (f"{self._name}, age: {self._age}, "
                f"article: {self._article}, term = {self._term},"
                f"number of victims = {self._victim}, death penalty = {self._death_penalty}")