class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        A = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            A[key].append(s)
        return list(A.values())