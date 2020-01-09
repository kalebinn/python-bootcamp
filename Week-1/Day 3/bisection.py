# finding the roots of a function between a specific region 
import math

def f(x):
    return math.sin(x)
 
def find_root(a, b): 
    c = (a + b)/2 # initial c
    ans = f(c) # f(c)

    num_iterations = 0
    while ans != 0 and num_iterations < 1000:
        num_iterations += 1
        #print("iteration:", num_iterations, "c =", c, "f(c)", f(c))
        c = (a + b)/2 
        ans = f(c)

        if (f(a)*ans > 0): # same sign
            a = c
        else: # diff sign
            b = c

    return c

lower = 3
upper = 10

print(find_root(lower, upper))
