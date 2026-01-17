class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0 
        a = []
        while l<len(word1) or r<len(word2):
            if l< len(word1):
                a.append(word1[l])
            if r< len(word2):
                a.append(word2[r])
            l+=1
            r+=1
        return ''.join(a)
            
