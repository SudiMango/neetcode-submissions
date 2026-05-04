class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker = defaultdict(int)

        for i in nums:
            tracker[i] += 1

        for k, v in tracker.items():
            if v > 1:
                return True

        return False