# TODO: Make a function that takes in 2 inputs: An lower limit and 
# an upper limit. The function should return a list of all multiples of 5
# between lower and upper limit (inclusive)

def find_mults(lower, upper):
    mults = []

    for nums in range(lower, upper+1):
        if nums % 5 == 0:
            mults.append(nums)
    
    return mults 

# testing the function:
print(find_mults(0,100))
#find_mults(0,1000)