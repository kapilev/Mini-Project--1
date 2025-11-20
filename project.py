import random

def play_game():
    choices = ["rock", "paper", "scissor"]
    user = input("Enter your choice (rock/paper/scissor): ").lower()
    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("It's a Tie!")
    elif (user == "rock" and computer == "scissor") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissor" and computer == "paper"):
        print("You Win!")
    else:
        print("You Lose!")

play_game()
