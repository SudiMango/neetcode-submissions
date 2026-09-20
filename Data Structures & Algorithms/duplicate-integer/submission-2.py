class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_map = defaultdict(int)

        for n in nums:
            dup_map[n] += 1

            if dup_map[n] > 1:
                return True

        return False