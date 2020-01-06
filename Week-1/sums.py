# the goal of this script is to sum up all the numbers between 
# N and M (inclusively), where N and M are both user inputs.

N = int(input("Enter lower limit: "))
M = int(input("Enter Upper limit: "))

print("using a for loop ")
sum = 0
for num in range(N, M+1):
    sum += num 

print("The total sum is: ", sum)

print("\nusing a while loop ")
sum = 0
num = N
while num <= M:
    sum += num
    num += 1

print("The total sum is: ", sum)