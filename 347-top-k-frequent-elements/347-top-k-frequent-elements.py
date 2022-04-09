class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        print(count)
        count = sorted(dict(count).items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in count[:k]]