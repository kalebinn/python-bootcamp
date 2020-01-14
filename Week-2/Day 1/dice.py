import random

def roll_dice():
    return random.randint(1,6)

def roll_dice_choice():
    """
    rolls a dice using the choice function from the random module
    """
    return random.choice([1,2,3,4,5,6])

def monte_carlo_with_lists(n):
    results = []
    for exp in range(0,n):
        results.append(roll_dice())
    print(f"Probability of 1 = {(results.count(1)/n) * 100} %")
    print(f"Probability of 2 = {(results.count(2)/n) * 100} %")
    print(f"Probability of 3 = {(results.count(3)/n) * 100} %")
    print(f"Probability of 4 = {(results.count(4)/n) * 100} %")
    print(f"Probability of 5 = {(results.count(5)/n) * 100} %")
    print(f"Probability of 6 = {(results.count(6)/n) * 100} %")

print(f"1/6 = {1/6}")
monte_carlo_with_lists(100000)