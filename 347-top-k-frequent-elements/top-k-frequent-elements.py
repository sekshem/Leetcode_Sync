class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            mp[nums[i]] = mp.get(nums[i],0) + 1
        a = sorted(mp.keys(), key = lambda x: mp[x], reverse = True)
        b = a[:k]
        return b 
        