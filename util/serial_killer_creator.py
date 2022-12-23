import random
from model.entity import *

class SerialKillerCreator:
    @staticmethod
    def create(size):
        NAMES = ("Ted Bundy", "Jack the Ripper", "Jeffrey Dahmer", "Harold Shipman",
                 "John Wayne Gacy","Pedro Lopez", "Ed Gein", "Aileen Wuornos",
                 "The Zodiac", "Edmund Kemper", "Albert Fish", "Gary Ridgway", "Сhikatilo",
                 "Hannibal Lector")

        MAX_AGE = 100
        MIN_AGE = 16

        MIN_VICTIM = 3
        MAX_VICTIM = 30

        MIN_TERM = 6
        MAX_TERM = 100

        ls = []

        for _ in range(size):
            name = random.choice(NAMES)
            age = random.randint(MIN_AGE, MAX_AGE)
            victim = random.randint(MIN_VICTIM, MAX_VICTIM)
            term = random.randint(MIN_TERM, MAX_TERM)
            death_penalty = random.randrange(2)
            serialkiller = SerialKiller(name, age, term, victim, death_penalty)
            ls.append(serialkiller)
        return ls