# The goal of this script is to print all the odd numbers between 
# 0 and N inclusively, where N is the user input

N = int(input("Enter a upper limit: "))

# Use a For loop first
print("Using a for loop: ")
for number in range(0,N+1):
    if (number % 2 == 1):
        print(number)

# Use a while loops:
print("\nUsing a while loop: ")
number = 1
while number <= N:
    if (number % 2 == 1):
        print(number)
    number += 1 