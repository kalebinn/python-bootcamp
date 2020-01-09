import random

winning_num = random.randint(0,100)
#print("The winning number is ", winning_num)

total_guesses = 10
guesses = []
user_won = False
guesses_taken = 0

while guesses_taken < total_guesses and user_won == False:
    user_guess = int(input("Enter your guess: "))
    guesses.append(user_guess)
    guesses_taken += 1
    if user_guess == winning_num:
        user_won = True
        print("Congrats, you won!") 
    elif user_guess >= winning_num - 5 and user_guess <=  winning_num +5:
        print("Hot")
    elif user_guess >= winning_num - 10 and user_guess <= winning_num + 10:
        print("Warm")
    else:
        print("Cold")

print("You took", guesses_taken)
print("Your guesses were: ")
print(guesses)
print("The winning number was:", winning_num)


