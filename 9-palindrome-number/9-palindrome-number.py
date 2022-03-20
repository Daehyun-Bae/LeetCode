class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        strNum = str(x)
        for i in range(len(strNum)):
            if strNum[i] != strNum[len(strNum)-1-i]:
                return False
    
        return True