# import the random module
import random 

winning_number = random.randint(0,10)
print(winning_number)

num_guesses = 5
user_won = False

while num_guesses != 0 and user_won == False:
    user_guess = int(input("Enter your guess: "))
    if user_guess == winning_number:
        print("Hey, you won!")
        user_won = True
    else:
        num_guesses -= 1
        if num_guesses == 0:
            print("Nope, you lost.")
        else:
            print("Nope, try again.")












