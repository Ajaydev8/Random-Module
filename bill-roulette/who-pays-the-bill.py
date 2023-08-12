# Import the random module here

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Names is a list and form that list I need the random member's name ok? So what are the options?

random_number = random.randint(0, 4)
bill_payer = names[random_number]

print(f"{bill_payer} is gonna pay the bill.")
