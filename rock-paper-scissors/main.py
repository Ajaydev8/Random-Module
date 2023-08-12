# Rock Paper Scissors ASCII Art

import random


# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")



# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

list = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, Type 1 for Paper, Type 2 for scissors "))
computer_choice = random.randint(0, 2)

list_2 = ["rock", "paper", "scissors"]

print(f"User Choice is {list_2[user_choice]}: ")
print(list[user_choice])


print(f"Computer choice is {list_2[computer_choice]}: ")
print(list[computer_choice])

if user_choice == computer_choice:
    print("It's a Tie!")
elif user_choice == 0 and computer_choice == 1:
    print("Sorry Computer wins")
elif user_choice == 1 and computer_choice == 2:
    print("Computer wins Better luck next time!")
elif user_choice == 2 and computer_choice == 0:
    print("Computer wins Better luck next time.")
else:
    print("Hooray you win.")

