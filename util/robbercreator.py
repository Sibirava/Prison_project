import random
from model.entity import *

class RobberCreator:
    @staticmethod
    def create(size):
        NAMES = ("John Dillinger", "Patty Hearst", "Baby Face Nelson", "Bonnie Parker",
                 "Clyde Barrow","Stanley Mark Rifkin", "Danny Ocean", "Robert Ryan",
                 "Virgil Malloy", "Tokio", "Berlin", "Nairobi", "Professor", "Rio", "Denver")

        MAX_AGE = 80
        MIN_AGE = 16

        MIN_HOSTAGE = 0
        MAX_HOSTAGE = 30

        MIN_TERM = 2
        MAX_TERM = 10

        MIN_STOLEN_MONEY = 1000
        MAX_STOLEN_MONEY = 165_000_000


        ls = []

        for _ in range(size):
            name = random.choice(NAMES)
            age = random.randint(MIN_AGE, MAX_AGE)
            article = 5
            term = random.randint(MIN_TERM, MAX_TERM)
            stolen_money = random.randint(MIN_STOLEN_MONEY, MAX_STOLEN_MONEY)
            hostage = random.randint(MIN_HOSTAGE, MAX_HOSTAGE)
            robber = Robber(name, age, article, term, stolen_money, hostage)
            ls.append(robber)
        return ls