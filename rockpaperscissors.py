import random
from secrets import choice

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock , paper, scissor?: ").lower()

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("TIE")
    elif player == "rock":
        print("computer: ", computer)
        print("player: ", player)
        if(computer == "scissors"):
            print("You Win!")
        if(computer == "paper"):
            print("oh o, You lose")
    elif player == "paper":
        print("computer: ", computer)
        print("player: ", player)
        if(computer == "rock"):
            print("You Win!")
        if(computer == "scissors"):
            print("oh o, You lose")
    elif player == "scissors":
        print("computer: ", computer)
        print("player: ", player)
        if(computer == "paper"):
            print("You Win!")
        if(computer == "rock"):
            print("oh o, You lose")
        
    yesorno = input("Play again? (Yes/No) " ).lower()

    if yesorno != "yes":
        break