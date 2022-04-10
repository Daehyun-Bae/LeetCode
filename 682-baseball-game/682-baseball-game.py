class Solution:
    def calPoints(self, ops: List[str]) -> int:
        score = []
        for op in ops:
            if op == "+":
                score.append(score[len(score)-1]+score[len(score)-2])
            elif op == "D":
                score.append(score[len(score)-1] * 2)
            elif op == "C":
                score.pop()
            else:
                score.append(int(op))

        return sum(score)