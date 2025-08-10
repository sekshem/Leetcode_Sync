class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = set()
        for i in nums:
            if i in hm:
                return True
            else: 
                hm.add(i)
        return False