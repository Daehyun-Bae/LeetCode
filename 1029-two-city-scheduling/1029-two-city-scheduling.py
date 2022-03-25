class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = list(map(lambda l: l[0] - l[1], costs))
        diff = [(v, i) for i, v in enumerate(diff)]
        sort = sorted(diff, key=lambda x: x[0])
        cost = 0
        for i in range(len(sort)):
            idx = sort[i][1]
            if i < len(sort)//2:
                cost += costs[idx][0]
            else:
                cost += costs[idx][1]
        return cost
