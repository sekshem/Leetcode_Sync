class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_map = {}
        n = len(nums)
        for i in nums:
            count_map[i] = count_map.get(i,0)+1

            if count_map[i] > n//2:
                return i
        return None