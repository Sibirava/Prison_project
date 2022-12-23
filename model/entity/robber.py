from model.entity import *


class Robber(Prisoner):
    def __init__(self, name, age, article, term, stolen_money, hostage=0, ):
        self._name = name
        self._age = age
        self._term = term
        self._article = article
        self._stolen_money = stolen_money
        self._hostage = hostage


    @property
    def stolen_money(self):
        return self._stolen_money

    @stolen_money.setter
    def stolen_money(self, stolen_money):
        if stolen_money > 0:
            self._stolen_money = stolen_money
        else:
            raise Exception("Wrong data")

    @property
    def hostage(self):
        return self._hostage

    @hostage.setter
    def hostage(self, hostage):
        self._hostage = hostage

    def __str__(self):
        return (f"{self._name}, age: {self._age}, "
                f"article: {self._article}, term = {self._term}, "
                f"stolen money = {self._stolen_money} $, amount of hostages {self._hostage}")
