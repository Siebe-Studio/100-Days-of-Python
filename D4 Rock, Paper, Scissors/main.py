import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]
selected = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

your_choice = int(selected)
computer_choice = random.randint(0,2)


if your_choice >= 3 or your_choice < 0:
    print("Your input was invalid.. You lose!")
else:

    print(f"You chose: \n{options[int(your_choice)]}")
    print(f"Computer chose:\n{options[computer_choice]}")

    if your_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and your_choice == 2:
        print("You lose.")
    elif computer_choice > your_choice:
        print("You lose.")
    elif computer_choice < your_choice:
        print("You win!")
    elif computer_choice == computer_choice:
        print("It's a draw!")



