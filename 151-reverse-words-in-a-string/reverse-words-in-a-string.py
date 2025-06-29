class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.strip().split()
        l = 0
        r = len(arr) -1
        res = ""
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            r-=1
            l+=1
        for i in range(len(arr)):
            res+=" " + arr[i]
        return res.strip()