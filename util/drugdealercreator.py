import random
from model.entity import *

class DrugdealerCreator:
    @staticmethod
    def create(size):
        NAMES = ("Miguel Ángel Félix Gallardo", "Pablo Escobar Gaviria", "Joaquín El Chapo Guzmán",
                 "Osiel Cárdenas Guillén", "Jorge Alberto Rodriguez", "Marcola", "Griselda Blanco",
                 "Roberto Suárez Gómez")

        MAX_AGE = 100
        MIN_AGE = 16

        MIN_TERM = 8
        MAX_TERM = 20

        ls = []

        for _ in range(size):
            name = random.choice(NAMES)
            age = random.randint(MIN_AGE, MAX_AGE)
            term = random.randint(MIN_TERM, MAX_TERM)
            drugdealer = Drugdealer(name, age, term)
            ls.append(drugdealer)
        return ls