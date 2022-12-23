import random
from model.entity import *

class KillerCreator:
    @staticmethod
    def create(size):
        NAMES = ("David Chapman", "Kevin James Loibl", "Nathan Gale", "Robert John Bardo",
                 "Nikolai Martynov","Rodion Roskolnikov", "Dantes", "Graf Monte Kristo",
                 "Brutus", "Herasim", "Djey Gatsbi", "Clayd Griffits")

        MAX_AGE = 100
        MIN_AGE = 16

        MIN_VICTIM = 1
        MAX_VICTIM = 3

        MIN_TERM = 3
        MAX_TERM = 50

        ls = []

        for _ in range(size):
            name = random.choice(NAMES)
            age = random.randint(MIN_AGE, MAX_AGE)
            victim = random.randint(MIN_VICTIM, MAX_VICTIM)
            term = random.randint(MIN_TERM, MAX_TERM)
            killer = Killer(name, age, term, victim)
            ls.append(killer)
        return ls