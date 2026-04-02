# Slow–Fast Pointers 
# scanning + building/modifying in-place
# Need to modify array in-place
# Remove / shift elements
# Maintain order
# One pass solution

# Remove Duplicates from Sorted Array:
def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(1,len(nums)):
            if nums[fast] != nums[slow]:
                slow+=1
                nums[slow] = nums[fast]

        return slow + 1

# Move Zeroes
def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(1,len(nums)):
            if nums[slow] == 0 and nums[fast] !=0:
                nums[slow],nums[fast] = nums[fast],nums[slow]
                slow += 1
        