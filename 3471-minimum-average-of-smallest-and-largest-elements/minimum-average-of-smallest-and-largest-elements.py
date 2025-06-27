class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        l,r = 0, len(nums)-1
        averages = []
        while l < r: 
            a = (nums[l] + nums[r])/2
            averages.append(a)
            l+=1
            r-=1
        b = min(averages)
        return b