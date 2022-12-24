from model.entity import *

class Judge:
    @staticmethod
    def calculate_total_term(prison):    # не понимаю, почему не считает тюрьму тюрьмой и всегда выдает -1
        if not isinstance(prison, Prison):
            return -1

        total = 0

        for prisoner in prison:
            if isinstance(prisoner, Prisoner):
                total += prisoner.term
        return total


    @staticmethod
    def find_max_term(prisoners):
        if not isinstance(prisoners, (list, tuple)):
            return

        iterm = 0
        for index in range(1, len(prisoners)):
            current = prisoners[index].term
            max = prisoners[iterm].term

            if current > max:
                iterm = index
        return prisoners[iterm]

    @staticmethod
    def count_killers(prisoners):
        if not isinstance(prisoners, (list, tuple)):
            return

        count_killers = 0
        for pr in prisoners:
            if pr.article == 2 or pr.article == 3:
                count_killers += 1
        return count_killers

    @staticmethod
    def count_drugdealers(prisoners):
        if not isinstance(prisoners, (list, tuple)):
            return

        count_drugdealers = 0
        for pr in prisoners:
            if pr.article == 4:
                count_drugdealers += 1
        return count_drugdealers

    @staticmethod
    def count_robbers(prisoners):
        if not isinstance(prisoners, (list, tuple)):
            return

        count_robbers = 0
        for pr in prisoners:
            if pr.article == 5:
                count_robbers += 1
        return count_robbers

    @staticmethod
    def calculate_total_victims(prison):

        total_victim = 0

        for killer in prison:
            if isinstance(killer, Killer):
                total_victim += killer.victim
        return total_victim

    @staticmethod
    def count_death_penalties(serialkillers):
        count = 0
        if not isinstance(serialkillers, (list, tuple)):
            return -1

        for sk in serialkillers:
            if isinstance(sk, SerialKiller) and sk.death_penalty:
                count += 1
        return count

    def calculate_terms(prisoners):
        total = 0

        for prisoner in prisoners:
            if isinstance(prisoner, Prisoner):
                total += prisoner.term
        return total