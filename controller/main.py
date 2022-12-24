import random
from model.entity import *
from model.logic import Judge
from util import *

def main():
   MIN_PRISON = 1
   MAX_PRISON = 12
   NUMBER_KILLERS_PRISON = random.randrange(MIN_PRISON, MAX_PRISON)
   NUMBER_DRUGDILLERS_PRISON = random.randrange(MIN_PRISON, MAX_PRISON)
   NUMBER_SERIAL_KILLERS_PRISON = random.randrange(MIN_PRISON, MAX_PRISON)
   NUMBER_ROBBERS_PRISON = random.randrange(MIN_PRISON, MAX_PRISON)


   ls = (KillerCreator.create(NUMBER_KILLERS_PRISON) +
         SerialKillerCreator.create(NUMBER_SERIAL_KILLERS_PRISON)
         + DrugdealerCreator.create(NUMBER_DRUGDILLERS_PRISON)
         + RobberCreator.create(NUMBER_ROBBERS_PRISON))
   print(Converter.convert_to_string(ls))

   print(f"\nTotal term for all the prisoners: {Judge.calculate_terms(ls)} years")

   print(f"\nMax terms has: {Judge.find_max_term(ls)}")

   print(f"\nThere are {Judge.count_killers(ls)} killers and {Judge.count_drugdealers(ls)} drugdealers "
         f"and {Judge.count_robbers(ls)} robbers in prison")

   print(f"\nTotal amount of victims among {Judge.count_killers(ls)} killers is "
         f"{Judge.calculate_total_victims(ls)}")
   print(f"\nThe amount of death penalties in prison is {Judge.count_death_penalties(ls)}")

if __name__ == "__main__":
   main()