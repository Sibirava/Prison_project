from model.entity import *

class Drugdealer(Prisoner):
    def __init__(self, name, age, term, article=4):
        self._name = name
        self._age = age
        self._article = article
        self._term = term

    def __str__(self):
        return (f"{self._name}, age: {self._age}, "
                f"article: {self._article}, term = {self._term},")