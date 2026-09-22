class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        num_set = set(nums)
        starting_nums = []

        for n in num_set:
            if n - 1 not in num_set:
                starting_nums.append(n)

        lens = [1 for _ in range(len(starting_nums))]
        for i, n in enumerate(starting_nums):
            curr = n
            while curr + 1 in num_set:
                lens[i] += 1
                curr += 1

        return max(lens)

        
