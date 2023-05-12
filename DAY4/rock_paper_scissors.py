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
game_images = [rock, paper, scissors]
game_name = ["Rock", "Paper", "Scissor"]

flag = True
while flag:
    print("Welcome to tha Rock Paper and Scissor game!")
    user_choice = int(input("What do you choose?\n"
    "Type - \ ""(0 for Rock)" "(1 for Paper)\n" "(2 for Scissors)" "(-1 for " "stop)\n"))

    if user_choice > 2 or user_choice < 0:
        print("You typed an invalid number, you lose!")

        flag = False

        if user_choice == -1:
            print("Thanks for playing")
            flag = False

    else:
        print(f"User Choice is :{game_name[user_choice]}")
        print(game_images[user_choice])

        computer_choice = random.randint(0, 2)
        print(f"Computer chose: {game_name[computer_choice]}")
        print(game_images[computer_choice])

        if user_choice == 0 and computer_choice == 2:
            print("You win!")

        elif computer_choice == 0 and user_choice == 2:
            print("You lose")

        elif computer_choice > user_choice:
            print("You lose")

        elif user_choice > computer_choice:
            print("You win!")

        elif computer_choice == user_choice:
            print("It's a draw")
