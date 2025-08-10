class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_map = {}
        n = len(nums)
    
    # Count frequencies
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
        
        # Early return optimization: if we already found majority
            if count_map[num] > n // 2:
                return num
    
        return None