# February 14th, 2025
# Spiro Kontossoros
# Python program file
# This program takes a list of given elements
# And sorts for the minimum (lowest) element in
# the list.

def minimum(element_list):
    """Finds the lowest number within a list of elements"""
    # Variable tracking the lowest element currently
    # recorded in the list
    lowest_element = element_list[0]

    # Loop that updates lowest_element by the
    # next lowest element found in the list
    for i in range(len(element_list)-1):
        # If current lowest_element is higher than current index,
        # lowest_element becomes the current index
        if lowest_element > element_list[i+1]:
            lowest_element = element_list[i+1]

    # Return the lowest found element
    return lowest_element

# print(minimum([]))

