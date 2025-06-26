from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        n = len(nums)
        # Move all non-zero elements to the front
        for r in range(n): 
            if nums[r] != 0:
                nums[l] = nums[r]
                l += 1
        # Fill the remaining positions with zeros
        for i in range(l, n):
            nums[i] = 0
