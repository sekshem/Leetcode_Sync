class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        i=0
        j=0
        while(j<len(haystack)):
            if(haystack[j]==needle[i]):
                if(i<len(needle)):
                    i=i+1
                if(i==len(needle)):
                    return(j-len(needle)+1)
            else:
                j=j-i
                i=0
            j=j+1
        return -1