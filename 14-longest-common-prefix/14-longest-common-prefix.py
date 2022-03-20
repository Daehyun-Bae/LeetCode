class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        maxLen = min(list(map(len, strs)))
        for i in range(maxLen):
            chrSet = set(list(map(lambda x: x[i], strs)))
            if len(chrSet) == 1:
                result += chrSet.pop()
            else:
                break

        return result
