from random import choice

choices = ("rock", "paper", "scissors")
print("Rock crushes scissors. Scissors cut paper. Paper covers rock")

player = input(
    'Enter your choice, Rock, Paper or Scissors. Type quit to leave the game.')
player = player.lower()
while player != "quit":
    computer = choice(choices)
    print("You chose " + player + ", and the computer chose " + computer+".")
    if player == computer:
        print("its a tie")
    elif player == "rock":
        if computer == "scissors":
            print('you win')
        else:
            print("computer won")
    elif player == "paper":
        if computer == 'rock':
            print('you won!!')
        else:
            print('computer wins')
    elif player == "scissors":
        if computer == 'paper':
            print("you won")
        else:
            print('computer won')
    else:
        print('error occured')

    print()
    player = input(
        'Enter your choice, Rock, Paper or Scissors. Type quit to leave the game.')
