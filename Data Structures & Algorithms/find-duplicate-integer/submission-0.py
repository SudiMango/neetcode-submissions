class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_to_freq = defaultdict(int)

        for n in nums:
            num_to_freq[n] += 1
        
        for k, v in num_to_freq.items():
            if v > 1:
                return k
        
        return 0