import random

winning_number = random.randint(0,100)
print(winning_number)
guesses_taken = 0
num_guesses = 10
user_won = False
guesses = []

while guesses_taken < num_guesses and user_won != True:
    user_guess = int(input("Enter your guess: "))
    guesses_taken += 1
    guesses.append(user_guess)
    if (user_guess == winning_number):
        print("Congrats! You won!")
        user_won= True
    elif user_guess >= winning_number-5 and user_guess <= winning_number+5:
        print("You're hot!")
    elif user_guess >= winning_number-10 and user_guess <= winning_number+10:
        print("You're warm!")
    else:
        print("Try again :(")

print("You took", guesses_taken)
print("Your guesses were:")
print(guesses)
print("But the winning number was", winning_number)
