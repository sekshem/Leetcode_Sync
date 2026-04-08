class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = 0
        m = 0
        r = n-1
        while m <= r:
            if nums[m] == 0:
                nums[m], nums[l] = nums[l], nums[m]
                m+=1
                l+=1
            elif nums[m] == 1:
                m+=1
            else:
                nums[r], nums[m] = nums[m], nums[r]
                r-=1
                