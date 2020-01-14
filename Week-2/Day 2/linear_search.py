# review of the linear search algorithm from previous week
def search(list, x):
    """
    implementation of the linear search algorithm.
    \tPARAM - list - list of elements to search through
    \tPARAM - x - element to search for
    \tRETURN - index of the element in the array (or None if not found)
    """
    for index in range(0, len(list)):
        if list[index] == x:
            return index 

    return None 