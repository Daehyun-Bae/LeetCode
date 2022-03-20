class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0): return False
        '''
        strNum = str(x)
        for i in range(len(strNum)//2):
            if strNum[i] != strNum[len(strNum)-1-i]:
                return False
    
        return True
        '''
        # another solution
        y = 0
        while x > y:
            y = y * 10 + x % 10
            x //= 10
        return x == y or x == y // 10
            