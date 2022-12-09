from model.entity import *

class Judge:
    @staticmethod
    def calculate_total_term(prison):
        if not isinstance(prison, Prison):
            return -1

        total = 0

        for prisoner in prison:
            if isinstance(prisoner, Prisoner):
                total += prisoner.term
        return total
