class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        for i in s:
            char_count[i] = char_count.get(i,0) + 1
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i
        return -1