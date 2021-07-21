from random import randint
secret_number = randint(1, 10)

# v1.0 secret_number = 7

# v2.0
# guess = int(input("What number am I thinking of?\n>> "))
#    if secret_number == guess:
#         print("Yay! You got it!!")
#     else:
#         print("Sorry, better luck next time")

while True:
    guess = int(input("What number am I thinking of?\n>> "))
    if secret_number == guess:
        print("Yay! You got it!!")
        break
    elif secret_number > guess:
        print('No thats too low.')
    elif secret_number < guess:
        print('No thats too high.')
    else:
        print("Sorry mate, try again!")
