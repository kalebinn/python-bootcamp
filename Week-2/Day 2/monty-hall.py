import random

def organize_game():
    # one door will have the money, the others will have nothing:
    door_contents = [1, 0, 0]

    # the random.shuffle() function shuffles the indices of the list
    random.shuffle(door_contents)

    # use the linear search algorithm to find the door with the money
    for i in range(0, len(door_contents)):
        if door_contents[i] == 1:
            winning_door = i
    
    # return the list of door contents and the number of the winning door
    return door_contents, winning_door

def game_time():
    # the door numbers go from 0 to 2, they correspond to the "door contents"
    door_nums = [0, 1, 2]

    # runs the previously written function, to organize the game
    # which puts the contents behind the doors, and tells the host which door is
    # the winning door
    door_contents, winning_door = organize_game()

    # Simulated a contestant. The contestant will make a choice from 0 to 2, 
    # corresponding to the door numbers
    door_chosen = random.choice(door_nums)

    # make a list of the unavailable doors to be opened by the host
    unavailable_doors = [door_chosen, winning_door]

    # using sets to find the door number left over
    # this "door_to_open" returns as a set
    door_to_open = set(door_nums).difference(unavailable_doors)

    # we can use the pop() function to pop it out of the set, and 
    # make it an integer value.
    door_to_open = door_to_open.pop()

    # open the door we just picked
    opened_door = door_nums[door_to_open]
    
    # declare the variables that tells us whether the win would come from
    # switching, or staying. 
    switched_win = False
    stayed_win = False 

    # we need to see if we won by switching or by staying. 
    # First we simulate the switch.
    # We can't switch to either the door we already chose, or the door that's 
    # already opened. 
    unavailable_doors = [door_chosen, door_to_open]
    switched_choice = set(door_nums).difference(unavailable_doors)

    # switched_choice is currently a set, so we need to use the pop() function
    # to pop the number out of the set. 
    # switched_choice should be a set of 1
    switched_choice = switched_choice.pop()

    # use the index value we established from the switched_choice variable
    # to find out the contents of the door behind it.
    if door_contents[switched_choice] == 1:
        # this means that the user one by switching
        switched_win = True
    
    if door_contents[door_chosen] == 1:
        stayed_win = True
        
    return int(switched_win), int(stayed_win)
    
def monte_carlo(N):
    # we need to keep track of the number of wins from
    # switching and the number of wins from staying.
    total_switched_wins = 0
    total_stayed_wins = 0

    # now we need to play the game N number of times
    switched_win = 0
    stayed_win = 0
    for game_num in range(0,N):
        # determine if we won by switching, or won by staying
        switched_win, stayed_win = game_time()

        # if we won by switching, increment total switched wins
        if switched_win == 1:
            total_switched_wins += 1

        # if we won by staying, increment total stayed wins
        if stayed_win == 1:
            total_stayed_wins += 1
    
    # print out the results
    print(f"Out of {N} plays") 
    print(f"Switched win percentage = { (total_switched_wins/N) * 100 } %")
    print(f"Stayed win percentage = { (total_stayed_wins/N) * 100} %")
        

monte_carlo(1000000)