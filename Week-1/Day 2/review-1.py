# TODO: write a script that prints out the multiples of 3
# between 0 and N (inclusive), where N is a user input.

N = int(input("Enter the upper limit."))

for num in range(0,N+1):
    if num % 3 == 0:
        print(num)

counter = 0
while counter <= N:
    if counter % 3 == 0:
        print(counter)
    counter += 1
    