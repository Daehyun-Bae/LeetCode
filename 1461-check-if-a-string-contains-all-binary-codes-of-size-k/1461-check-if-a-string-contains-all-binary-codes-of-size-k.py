class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        binSet = set([s[i: i+k] for i in range(len(s) -k + 1)])
        return len(binSet) == 2**k