# the goal of this script is to print out the even numbers
# between 1 and N (inclusive), where N is a user input. 

N = int(input("Enter an upper limit: "))

print("using a for loop: ")
for number in range(1,N+1):
    if (number % 2 == 0):
        print(number)

# use a while loop to perform the same function
print("\nusing a while loop: ")
counter = 1
while counter <= N:
    if (counter % 2 == 0):
        print(counter)
    
    counter += 1
