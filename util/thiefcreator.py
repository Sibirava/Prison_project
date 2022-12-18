@staticmethod
def create(size):
    NAMES = ("Kate", "Alex", "Mary", "Alice", "Peter", "Ivan", "Victor",
             "Denis", "Tom", "Tim", "Max", "Jared", "Jensen", "Michel", "Alina")


    MAX_AGE = 130
    MIN_AGE = 0

    ls = []

    for _ in range(size):
        firstname = random.choice(NAMES)
        surname = ALFABET[random.randrange(len(ALFABET))]
        age = random.randint(MIN_AGE, MAX_AGE)
        alive = random.randrange(2)
        human = Human(firstname, surname, age, alive)
        ls.append(human)
    return ls