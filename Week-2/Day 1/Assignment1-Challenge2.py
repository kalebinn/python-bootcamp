# programming challenge # 2
def find_odds(n):
    odds = []

    for num in range(0,n+1):
        if (num % 2 == 1):
            odds.append(num)
    
    return odds

n = 19
print(find_odds(n))