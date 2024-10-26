#!/usr/bin/env python
# coding: utf-8


# code obtained from Github https://github.com/leeshibley/runtime-analyzer/blob/master/SortingMethods.py
# code partially modified to include only selection sort and quick sort classes that self implement the algorithms

"""A class of self-implemented sorting algorithms, including:
    * Selection Sort
    * Quick Sort
    """
class SortingMethod:
    
    def __init__(self, nums):
        self.nums = nums
    
    def selectionsort(self):
        """
        Runtimes:
        * best case ------- O(n^2)
        * average case ---  O(n^2)
        * worst case ------ O(n^2)
        """
        spot_marker = 0
        
        while spot_marker < len(self.nums):
            for i in range(spot_marker, len(self.nums)):
                if self.nums[i] < self.nums[spot_marker]:
                    self.nums[spot_marker], self.nums[i] = self.nums[i], self.nums[spot_marker]
            spot_marker += 1
        
        return self.nums
                
    def quicksorted(self, nums):
        """A helper to the quicksort() function.
        Recursively sorts and combines the 'smaller than', 'equal to', and 'larger than' lists via Quick Sort.
        """
        
        # different method for quick used compared to experiment 1 as this one uses built in python functions to sort the array
        if len(nums) < 2:
            return nums
        else:
            pivot = nums[-1]
            smaller, equal, larger = [], [], []
            
            for i in nums:
                if i < pivot:
                    smaller.append(i)
                elif i == pivot:
                    equal.append(i)
                else:
                    larger.append(i)
            return self.quicksorted(smaller) + equal + self.quicksorted(larger)
        
    def quicksort(self):
        """
        Runtimes:
        * best case ------- O(nlog(n))
        * average case ---  O(nlog(n))
        * worst case ------ O(n^2) (very rare, often avoidable)
        """
        return self.quicksorted(self.nums)