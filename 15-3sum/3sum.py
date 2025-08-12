class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        result_set = set()
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            seen = set()
            for j in range(i+1,len(nums)):
                complement = -(nums[i]+nums[j])

                if complement in seen:
                    triplet = tuple(sorted([nums[i], nums[j],complement]))
                    result_set.add(triplet)
                seen.add(nums[j])
        return [list(triplet) for triplet in result_set]