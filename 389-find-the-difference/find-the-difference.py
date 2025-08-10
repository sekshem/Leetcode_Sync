class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        countS = Counter(s)
        countT = Counter(t)
        for c in countT:
            if c not in countS:
                return c
            if countS[c] < countT[c]:
                return c