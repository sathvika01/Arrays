# TWO POINTERS
# Used for Sorted Arrays, Pairs / removing duplicates
# searching / comparing from both ends

#1. Two Sum II (Sorted Array)
#👉 Problem:
#Given a sorted array, find two numbers that sum to target.

# def two_sum(arr,target):
#     left, right = 0, len(arr)-1

#     while left < right:
#         s = arr[left] + arr[right]
#         if s == target:
#             return [left,right]
#         elif s < target:
#             left += 1
#         else: 
#             right -= 1
        
# arr = [1,2,3,4,5]
# result = print(two_sum(arr,target=7))


#If the problem says 1 indexed array that means index starts from 1 not zero
# therefore return [left+1, right+1]


# 3SUM
# arr = [-1,0,1,2,-1,-4]

# def three_sum(arr,target = 0):
#     arr.sort()
#     for i in range(len(arr)):
#         left =i+1
#         right = len(arr) -1
#         fixed = i
#         if arr[left] + arr[right] + arr[fixed] == 0:
#             return [arr[left],arr[right],arr[fixed]]
#         elif arr[left] + arr[right] < -(arr[fixed]):
#             left +=1
#         else:
#             right -=1

# result = three_sum(arr,target=0)
# print(result)

#Check PALINDROME
def isPalindrome(self, s: str) -> bool:
        clean = ""
        for ch in s:
            if ch.isalnum():
                clean = clean + ch.lower()
                
        s = clean
        i=0
        j = len(s)-1
        while i<j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                return False
        return True
        



