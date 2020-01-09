# TODO: Write a function that takes a integer and a list as the input.
# the function should return the index of where the integer was found
# on the list

def search(x, list):
    """
    this function returns the index of where the element x was found
    on the list.
    \tparam : x - the element you're searching for
    \tparam : list - the list you're searching through
    \treturns : the index of where the element was found (if applicable)
    """
    for index in range(0,len(list)):
        if list[index] == x:
            return index 

def find_max(list):
    """
    this function returns the maximum element in the list

    \tparam : list - a list of numerical elements
    \treturns : the maximum value in the list
    """
    max = list[0]

    for element in list:
        if element >= max:
            max = element

    return max 

def find_min(list):
    """
    this function returns the minimum element in the list

    \tparam : list - a list of numerical elements
    \treturns : the minimum value in the list
    """
    min = list[0]

    for element in list:
        if element <= min:
            min = element

    return min 


