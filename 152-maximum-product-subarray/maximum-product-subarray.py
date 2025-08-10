class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currProd = 1
        maxProd = nums[0]
        
        # Forward pass
        for R in range(len(nums)):
            currProd = currProd * nums[R]
            maxProd = max(maxProd, currProd)
            if currProd == 0:  # Reset after zero
                currProd = 1
        
        # Backward pass to handle cases where optimal subarray excludes negatives
        currProd = 1
        for L in range(len(nums) - 1, -1, -1):
            currProd = currProd * nums[L]
            maxProd = max(maxProd, currProd)
            if currProd == 0:  # Reset after zero
                currProd = 1
                
        return maxProd