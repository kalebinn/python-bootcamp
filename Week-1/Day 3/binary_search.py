my_list = [1,2,3,4,5,6]

def binary_search(x, list):
    """
    iterative binary search
    """
    list_copy = list # make a copy of the list
    #print(list_copy)
    found = False

    while found == False:
        mid_index = len(list_copy)//2
        print(mid_index)

        if list_copy[mid_index] < x:
            list_copy = list_copy[mid_index:]
        elif list_copy[mid_index] > x:
            list_copy = list_copy[:mid_index]
        else:
            found = True
            return mid_index

    return None

print(binary_search(5,my_list))

        
