# Code obtained from Github https://github.com/HebaElwazzan/Sorting-Algorithms-Runtime/blob/master/plotting.py
# Code modified to include only bubble sort and quick sort algorithms

from matplotlib import pyplot as plt
import random
import time
import bubble
import quick

def copy_array(array):  # function to copy contents of array
    size = len(array)
    temp = [0] * size  # temporary array to pass to the functions
    for j in range(size):
        temp[j] = array[j]
    return temp

# Here, a random number generator function is used to assign values to an array
# The values of the array have been modified from 0-9 to 0-9999 to have an array with more variablity
# random number generator code modified to increase the size of the array
def generate_dataset(size):
    array = [0] * size  # initializing an array of zeros

    for i in range(size):  # loop to replace the zeros in array with random numbers
        array[i] = int(random.random() * 10000)  # random numbers from 0 - 9999
    if size == 10:
        print("Dataset to be sorted: ")
        print(array)
    return array

# function that runs specified sort and returns time in milliseconds taken for run
def run_sort(array, sorting_func, sorting_name):
    temp = copy_array(array)
    print("Now sorting using " + sorting_name + " array of size " + str(len(array)))
    if sorting_func == quick.sort_by_quicksort:
        start_time = time.time()
        sorting_func(temp, 0, len(array) - 1)
        end_time = time.time()
    else:
        start_time = time.time()
        sorting_func(temp)
        end_time = time.time()
    if len(temp) == 50:
        print("Sorted array using " + sorting_name)
        print(temp)
    runtime = (end_time - start_time) * 1000
    print("Runtime in milliseconds: " + str(runtime))
    print()
    return runtime


# this function generates different array sizes, sorts them with the 2 sorting techniques, then plots runtime against
# array size
# 10 different array size values used for the two sorting algorithms
# code for size_values chosen personally
def generate_data():

    size_values = [10, 50, 100, 1000, 5000, 10000, 20000, 30000, 50000, 100000] 
    bubble_values = []
    quick_values = []

    for value in size_values:
        array = generate_dataset(value)
        bubble_values.append(run_sort(array, bubble.bubble_sort, "bubble sort"))
        try:
            quick_values.append(run_sort(array, quick.sort_by_quicksort, "quick sort"))
        except RecursionError:
            print("Maximum recursion depth reached, quick sort cannot compute")
            quick_values.append(None)
     
    plt.plot(size_values, bubble_values, label="Bubble Sort")
    plt.plot(size_values, quick_values, label="Quick Sort")
    
    plt.title("Time Performance of Sorting Algorithms")
    plt.xlabel("Array size")
    plt.ylabel("Time (milliseconds)")
    plt.legend()
    plt.show()
