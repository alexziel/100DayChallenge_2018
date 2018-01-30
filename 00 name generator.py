''' Name generator ver. 1.0 '''

import random

fNames = ["Kayah", "Kunegunda", "Lina"]
fSurnames = ["Kowalska", "Malinowska", "Ibiszowska"]
mNames = ["Bulbazaur", "Pikaczu", "Digimon"]
mSurnames = ["Niezbędny", "Całkiemnowy", "Ibisz"]

"""
fNamesDim = ["Kajusia", "Kundzia", "Linka"]
fSurnamesDim = ["Kowalskusia", "Malinusiaa", "Ibiszusia"]
mNamesDim = ["Bulbazaurek", "Pikaczuś", "Digimonek"]
mSurnamesDim = ["Niezbędnniczkowy", "Całkiemnowiusi", "Ibiszek"]
"""


print('Welcome to name generator!\n')



def generatedName(letter):
    if letter == "f":
        fLetter = random.choice(fNames) + " " + random.choice(fSurnames)
        print(fLetter)

    elif letter == "m":
        mLetter = random.choice(mNames) + " " + random.choice(mSurnames)
        print(mLetter)
    else:
      print("Wrong letter :( Only 'w' or 'm' \n")

gender = input('Do you want to generate female or male name (f / m)? \n')
generatedName(gender)
choose = input("Generate again? Choose y for yes or press any key to exit. \n")

while choose == "y":
    gender = input("Choose gender to generate: f for female and m for male\n")
    generatedName(gender)
    choose = input("Generate again? Choose y for yes or type anything else to exit \n")
print("Bye!")
