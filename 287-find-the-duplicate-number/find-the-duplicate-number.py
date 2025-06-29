class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0 
        nums.sort()
        while i < len(nums):
            i+=1
            if nums[i] == nums[i-1]:
                return nums[i-1]