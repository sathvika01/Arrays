# TWO POINTERS
# Used for Sorted Arrays, Pairs / removing duplicates

#1. Two Sum II (Sorted Array)
#👉 Problem:
#Given a sorted array, find two numbers that sum to target.

def two_sum(arr,target):
    left, right = 0, len(arr)-1

    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return [left,right]
        elif s < target:
            left += 1
        else: 
            right += 1
        
arr = [1,2,3,4,5]
result = print(two_sum(arr,target=7))