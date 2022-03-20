class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        skip = False
        for i, c in enumerate(s):
            if skip: 
                skip = False
                continue
                
            if c == 'I':
                if i < len(s)-1 and s[i+1] == 'V':
                    skip = True
                    result += 4
                elif i < len(s)-1 and s[i+1] == 'X':
                    skip = True
                    result += 9
                else:
                    result += 1
            if c == 'V':
                result += 5
            if c == 'X':
                if i < len(s)-1 and s[i+1] == 'L':
                    skip = True
                    result += 40
                elif i < len(s)-1 and s[i+1] == 'C':
                    skip = True
                    result += 90
                else:
                    result += 10
            if c == 'L':
                result += 50
            if c == 'C':
                if i < len(s)-1 and s[i+1] == 'D':
                    skip = True
                    result += 400
                elif i < len(s)-1 and s[i+1] == 'M':
                    skip = True
                    result += 900
                else:
                    result += 100
            if c == 'D':
                result += 500
            if c == 'M':
                result += 1000
        return result