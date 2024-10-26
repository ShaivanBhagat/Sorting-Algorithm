def partition(array, first, last):  # function to split array into two parts (s1 < pivot and s2 >= pivot) and
    # determine place of pivot
    last_s1 = first  # sets end of s1
    first_unknown = first + 1  # determines start of part which does not belong to s1 or s2 yet

    while first_unknown <= last:  # loop to go over all unknown part
        if array[first_unknown] < array[first]:
            last_s1 += 1  # increases size of s1 to hold new element
            array[first_unknown], array[last_s1] = array[last_s1], array[first_unknown]  # swaps first element in
            # unknown part with last element in s1
        first_unknown += 1  # point to next element in unknown part

    array[first], array[last_s1] = array[last_s1], array[first]  # swaps first element in array (pivot) with last
    # element in s1 for pivot to be between s1 and s2
    return last_s1

# sorting the array 
def sort_by_quicksort(array, first, last):
    if first < last:
        pivot = partition(array, first, last)   # places pivot in the middle of array
        sort_by_quicksort(array, first, pivot - 1)  # sorts first half of array
        sort_by_quicksort(array, pivot + 1, last)  # sorts second half of array
