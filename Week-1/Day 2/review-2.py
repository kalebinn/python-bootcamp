# TODO: Write a script that prints out the common multiples of 3 
# and 5 between the range 0 and N (inclusive). Where N is a 
# user input

N = int(input("Enter the upper limit: "))

for num in range(0,N+1) :
    if (num % 3 == 0) and (num % 5 == 0):
        print(num) 