print('Guessing game') 
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 



import random

hidden_number = (random.randrange(1,11))

print(hidden_number)

i=1
while i <= 3:
    guess = int(input("Choose a number between 0-10: "))
    if guess == hidden_number:
            print("You win!")
            break
    elif i == 3:
         print(f"You lose! $100 TO PLAY AGAIN!")
         break
    else:
        print(f"Try again. That was guess {i} out of 3.")
        i=i+1


# print(and input boxes) 1. If user wins 2. If user loses
#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
#coming back to try this ^^