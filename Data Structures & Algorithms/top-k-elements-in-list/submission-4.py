class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_frequency = defaultdict(int)
        freq_index_to_value: List[List[int]] = [[] for _ in range(len(nums) + 1)]
        ret = []

        for n in nums:
            num_to_frequency[n] += 1

        for key, value in num_to_frequency.items():
            freq_index_to_value[value].append(key)

        iterations = 0
        for v in reversed(freq_index_to_value):
            if len(v) == 0:
                continue

            for v2 in v:
                ret.append(v2)
                iterations += 1
                if iterations == k:
                    break

            if iterations == k:
                    break
        
        return ret

        
        

            
        