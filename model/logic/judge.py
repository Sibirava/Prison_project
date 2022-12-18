from model.entity import *


class Judge:
    @staticmethod
    def calculate_total_term(prison):
        # if not isinstance(prison, Prison):
        #     return -1

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
            if pr.article == 2:
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
    def calculate_total_victims(prison):

        total_victim = 0

        for killer in prison:
            if isinstance(killer, Killer):
                total_victim += killer.victim
        return total_victim