# define f(x) = x + 1
def f(x):
    ans = x + 1 
    return ans 

my_solution = f(1)
#print(my_solution)

# try for yourself:
# define a function of x, where
# g(x) = x^4 + x^2 + 1 
# NOTE: carrots aren't for exponents in python

def g(x):
    return (x**4 + x**2 + 1)

#print(g(1), g(2), g(3))

# function with multiple returns
def get_first_two_evens():
    return 2, 4

even1, even2 = get_first_two_evens()
#print(even1)
#print(even2)

# function with no returns
def print_even(N):
    for num in range(1, N+1):
        if num % 2 == 0:
            print(num)

#print_even(10) # 2,4,6,8,10

# TODO: Write a function that takes N as in an input and print
# all common multiples of 3 and 7, between 0 and N (inclusive)

def my_function():
    N = int(input("Enter your upper limit: "))
    for num in range(0,N+1):
        if (num % 3 == 0) and (num % 7 == 0):
            print(num)

#my_function()

# define a function that takes 3 inputs: x, y, N
# The function will find all the common multiples of x and y
# between 0 and N 

def find_multiples():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    N = int(input("Enter the upper limit: "))

    for num in range(0,N):
        if (num % x == 0) and (num % y == 0):
            print(num)

#find_multiples(3,7,100)
#find_multiples(2,3,10)
find_multiples()