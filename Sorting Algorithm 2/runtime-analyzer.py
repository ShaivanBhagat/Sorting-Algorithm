#!/usr/bin/env python
# coding: utf-8

# code obtained from Github from https://github.com/leeshibley/runtime-analyzer/blob/master/runtime-analyzer.py
# code modified partially to include only selection and quick sort and increase the length of the array and the maximum number possible in the array

import random
import time
import sys

import SortingMethods as sm

if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 8)

filename = "runtime_data.csv"

print("\n", "=" * 68)
length = int(input("How many values would you like to sort? "))

a = 0
b = int(input("What is the highest value you would like in the array? "))

n_runs = int(input("How many runs would you like to do? "))

print("\n", "=" * 68)

for n in range(n_runs):
    ## create new random list
    nums = []
    for i in range(length):
        nums.append(random.randint(a, b))
    alg = sm.SortingMethod(nums)

    print(f"Run {n + 1} of {n_runs}")
    
    runtime_string = f""

# length increased to 1000000 for running selection and quick sort to compensate for a larger possibility of array size and number

    if length <= 1000000:  ## Inefficient (O(n^2)) algorithms omitted for large n

        t_selectionsort_0 = time.time()
        alg.selectionsort()
        t_selectionsort_1 = time.time()
        
        selectionsort_time = t_selectionsort_1 - t_selectionsort_0
        print(f"Selection Sort --- {round(selectionsort_time, 4)} seconds")
        
        runtime_string = runtime_string + f",{selectionsort_time}"
    else:
        runtime_string = runtime_string + f",NA,NA,NA"


    if length <= 1000000:
        t_quicksort_0 = time.time()
        alg.quicksort()
        t_quicksort_1 = time.time()

        quicksort_time = t_quicksort_1 - t_quicksort_0
        print(f"Quick Sort ------- {round(quicksort_time, 4)} seconds")
        
        runtime_string = runtime_string + f",{quicksort_time}"
    else:
        runtime_string = runtime_string + f",NA"

    with open(f"{filename}", "a+") as f:
        data = f"{length},{b},{n + 1}" + runtime_string + "\n"
        f.write(data)
    f.close()
    print(f"Results written to file {filename}")

    print("=" * 68, "\n")
