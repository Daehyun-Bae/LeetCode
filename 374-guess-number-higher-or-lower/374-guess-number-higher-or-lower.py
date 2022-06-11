# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1 : return 1
        start = 1
        end = n + 1
        
        while start <= end:
            current = (start + end) // 2
            res = guess(current)
            if res == 0:
                return current
            elif res == 1:
                start = current
            elif res == -1:
                end = current
        