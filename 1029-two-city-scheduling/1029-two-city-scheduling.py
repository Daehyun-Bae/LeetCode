class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sort = sorted(costs, key=lambda x: x[0] - x[1])
        
        return sum(list(map(lambda x: x[0], sort[:len(costs)//2]))) + sum(list(map(lambda x: x[1], sort[len(costs)//2:])))
