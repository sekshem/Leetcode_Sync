class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_count = {}
        for i in magazine: 
            char_count[i] = char_count.get(i,0)+ 1
        for i in ransomNote:
            if char_count.get(i,0)<=0:
                return False
            char_count[i] -= 1
        return True