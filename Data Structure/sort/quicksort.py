
def quicksort(array = [3,4,6,2,54,77,24,56,34,5345,8,5,6,3,7,4,545,56,4,7,8,67]):
    less = [ ]
    greater = [ ]
    equal = [ ]

    if len(array) > 1 :
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x > pivot:
                greater.append(x)
            if x == pivot:
                equal.append(x)
        # Don't forget to return something!
        return quicksort(less) + equal + quicksort(greater) # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:# You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array
print(quicksort())
