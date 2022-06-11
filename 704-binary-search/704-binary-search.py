class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        if left == right:
            return 0

        while True:
            cur = (left + right) // 2
            v = nums[cur]
            if v == target:
                return cur
            elif left == cur:
                return -1
            elif v < target:
                left = cur
            elif v > target:
                right = cur