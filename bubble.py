# code for the bubble sorting algorithm obtained from Github https://github.com/HebaElwazzan/Sorting-Algorithms-Runtime/blob/master/bubble.py

def bubble_sort(arr):
    
    n = len(arr)
    for i in range(n - 1):
        flag = 0
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 1
        if not flag:
            break
