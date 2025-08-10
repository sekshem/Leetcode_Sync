class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        char_count = {}
        for i in jewels: 
            char_count[i] = True
        count = 0
        for j in stones:
            if char_count.get(j,False):
                count+=1
        return count        
