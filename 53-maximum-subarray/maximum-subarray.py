class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        L = 0 
        for R in range(len(nums)):
            curSum = max(curSum,0)
            curSum += nums[R]
            maxSum = max(maxSum,curSum)
        return maxSum