class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currProd = 1
        maxProd = nums[0]
        
        for R in range(len(nums)):
            currProd = currProd * nums[R]
            maxProd = max(currProd, maxProd)
            if currProd == 0:
                currProd = 1
        
        currProd = 1
        for L in range(len(nums)-1,-1,-1):
            currProd = currProd * nums[L]
            maxProd = max(currProd, maxProd)
            if currProd == 0:
                currProd = 1
        return maxProd