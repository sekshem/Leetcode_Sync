class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        cur = 0
        for i in range(len(nums)): 
            prefix[i] = cur
            cur += nums[i]
        cur = 0 
        for i in range(len(nums)-1,-1,-1):
            postfix[i] = cur
            cur += nums[i]
        for i in range(len(nums)):
            if prefix[i] == postfix[i]:
                return i
        return -1

