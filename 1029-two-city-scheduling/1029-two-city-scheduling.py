class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        return sum(list(map(lambda x: x[0], costs[:len(costs)//2]))) + sum(list(map(lambda x: x[1], costs[len(costs)//2:])))
