import random
from model.entity import *
from model.logic import Judge
from util import *

def main():
   MIN_PRISON = 5
   MAX_PRISON = 40
   NUMBER_KILLERS_PRISON = random.randrange(MIN_PRISON, MAX_PRISON)
   NUMBER_DRUGDILLERS_PRISON = random.randrange(MIN_PRISON, MAX_PRISON)

   ls = KillerCreator.create(NUMBER_KILLERS_PRISON) + DrugdealerCreator.create(NUMBER_DRUGDILLERS_PRISON)
   print(Converter.convert_to_string(ls))

   sum_term = Judge.calculate_total_term(ls)
   print(f"Total terms is: {sum_term} years")

   max_term = Judge.find_max_term(ls)
   print(f"Max terms has: {max_term}")

   print(f"There are {Judge.count_killers(ls)} killers and {Judge.count_drugdealers(ls)} drugdealers "
         f"in prison")

   print(f"Total amount of victims among {Judge.count_killers(ls)} killers is "
         f"{Judge.calculate_total_victims(ls)}")

if __name__ == "__main__":
    main()