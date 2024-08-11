import random
print("Welcome to Rock-Papers-Scissors Game")
print("====================================")
print("Game Rules:\n"
      "1.Rock vs Scissors ---> Rock wins against Scissors\n"
      "2.Paper vs Scissors ---> Scissors wins against Paper\n"
      "3.Rock vs Paper ---> Paper wins against Rock\n")
print("Choose your choice to start the game..")
user_choice = int(input("Enter Your Choice:\n"
                        "0 for Rock\n"
                        "1 for Paper\n"
                        "2 for Scissors.\n"))
print("You have chosen:",user_choice)
if user_choice >= 3 or user_choice < 0:
    print("You have entered an invalid number, You Lose...")
else:
    computer_choice = random.randint(0,2)
    print("Computer Chosen:",computer_choice)
    if computer_choice == user_choice:
        print("It's a tie..")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose..")
    elif user_choice == 0 and computer_choice == 2:
        print("You Win..")
    elif computer_choice  > user_choice:
        print("You Lose..")
    elif user_choice > computer_choice:
        print("You Win..")