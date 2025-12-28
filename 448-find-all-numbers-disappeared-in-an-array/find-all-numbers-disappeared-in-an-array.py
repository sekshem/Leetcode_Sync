class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        a = []
        for i in range(1,len(nums)+1):
            if i not in num_set:
                a.append(i)
        return a