import random

def organize_game():
    doors = [1,0,0]
    random.shuffle(doors)
    for i in range(len(doors)):
        if doors[i] == 1:
            door_with_car = i
    return doors, door_with_car

def game_time():
    door_numbers = [0,1,2]

    # organize the doors and open the one without the car
    doors, door_with_car = organize_game()
    #print(f"door with car = {door_with_car}")

    # choose a door
    door_chosen = random.choice(door_numbers)
    #print(f"Chosen door = {door_chosen}")

    # open a door that wasn't chosen and doesn't have a car
    door_to_open = set(door_numbers).difference([door_chosen, door_with_car])
    opened_door = door_to_open.pop()
    #print(f"Opening door #{opened_door}")

    # we can either switch or not switch
    # then see if the contenstant has won
    switched_win = False
    stayed_win = False
    final_choice = set(door_numbers).difference([door_chosen, opened_door])
    if doors[final_choice.pop()] == 1:
        switched_win = True

    final_choice = door_chosen
    if doors[final_choice] == 1:
        stayed_win = True

    return switched_win, stayed_win

def monte_carlo(n):
    # n is the number of times to run monte_carlo
    switched_win_count = 0
    stayed_win_count = 0
    for i in range(0,n):
        switched_win, stayed_win = game_time()
        switched_win_count += switched_win
        stayed_win_count += stayed_win

    print(f"--- Out of {n} plays ---")
    print(f"switched win = {(switched_win_count/n)*100}")
    print(f"stayed win = {(stayed_win_count/n)*100}")

monte_carlo(1000000)
