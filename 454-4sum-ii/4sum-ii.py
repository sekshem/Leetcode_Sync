class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_count = defaultdict(int)
        for num1 in nums1:
            for num2 in nums2: 
                sum_ab = num1 + num2
                sum_count[sum_ab] +=1
        count = 0 
        for num3 in nums3:
            for num4 in nums4:
                sum_cd = num3 + num4
                complement = -sum_cd
                count+=sum_count[complement]
        return count