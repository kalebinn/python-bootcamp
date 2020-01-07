# practicing with lists and functions

# EXAMPLE: Define a function that returns a list of even numbers
# between A and B (inclusive).

def find_evens(A,B):
    evens = []
    for nums in range(A,B+1):
        if (nums % 2 == 0):
            evens.append(nums)
    return evens 

#print(find_evens(2, 20))

# TODO: Define a function that returns a list of numbers between
# A and B (inclusive) that are even multiples of 3.

def even_mults(A,B):
    mults = []

    for nums in range(A,B+1):
        if (nums % 6 == 0):
            mults.append(nums)

    return mults

print(even_mults(0,20))
