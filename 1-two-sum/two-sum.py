class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in N:
                return [N[complement],i]
            N[num] = i
        return []
