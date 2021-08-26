import random

choices = ("rock", "paper", "scissors")
print("Rock crushes scissors. Scissors cut paper. Paper covers rock")


player = input('Enter your choice, Rock, Paper or Scissors. Type quit to leave the game.')

while player != "quit":
    player = player.lower()
    computer = random.choice(choices)
    print("You chose " +player+ ", and the computer chose " +computer+".")
    if player == computer:
        print("its a tie")
    elif player == "rock":
        if computer == "paper":
            print('computer wins')
        else:
            print("you won")
    elif player == "paper":
        if computer == 'rock':
            print('you won!!')
        else:
            print('computer wins')
    elif player == "scissors":
        if computer == 'rock':
            print("computer won")
        else:
            print('you won')
    else:
        print('error occured')
    finally:
        inp = input('do you want to continue again')
        if inp.
