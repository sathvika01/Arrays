arr = [10, 20, 30, 40]
print(arr[0])   # 10
print(arr[-1])  # 40

#Traversal (O(n)) this method used to modify elements
for i in range(len(arr)):
    print(arr[i])

# OR (better) this way you cant modify elements
for num in arr:
    print(num) 

for i,num in enumerate(arr):
    print(i,num)

#INSERTION
#At end (O(1))
arr.append(50)

# At specific position (O(n))
arr.insert(2,25)

#DELETION
# By value
arr.remove(20)

# By index
arr.pop(1)

#Delete last
arr.pop()

#Update
arr[1] = 90


# 3.SEARCHING
# Linear Search (O(n))
def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

result = search(arr, 90)
print(result)

# Binary Search (O(log n)) → ONLY if sorted
def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid -1
    return -1

result2 = print(binary_search(arr,50))