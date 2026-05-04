class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1


        longest = 1
        prev = sorted_nums[0]
        curr = 1
        for i in range(1, len(sorted_nums)):
            if prev == sorted_nums[i]:
                continue
            
            if prev + 1 == sorted_nums[i]:
                prev = sorted_nums[i]
                curr += 1
                if curr > longest:
                    longest = curr
            else:
                prev = sorted_nums[i]
                curr = 1

        return longest
