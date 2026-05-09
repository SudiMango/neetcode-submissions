class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_to_freq = defaultdict(int)

        for n in nums:
            num_to_freq[n] += 1
            if  num_to_freq[n] > 1:
                return n
        
        return 0