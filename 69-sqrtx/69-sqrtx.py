class Solution:
    def mySqrt(self, x: int) -> int:
        t = 1
        while (t < 2**16):
            if x < t*t:
                return t - 1
            t += 1
        
        return 2**16