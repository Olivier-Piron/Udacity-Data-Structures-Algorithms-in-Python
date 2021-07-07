"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    if array: 
        pivot = array[0]
        below = [i for i in array[1:] if i < pivot] 
        above = [i for i in array[1:] if i >= pivot]
        return quicksort(below) + [pivot] + quicksort(above)
    else: 
        return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)