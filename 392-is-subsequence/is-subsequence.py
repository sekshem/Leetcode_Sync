class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l,r,count=0,0,0
        while r < len(t) and l < len(s):
            if s[l] == t[r]:
               if l < len(s):
                 l+=1
                 r+=1
                 count +=1
            elif s[l] != t[r]:
                r+=1
        if count == len(s):
            return True
        else: return False
