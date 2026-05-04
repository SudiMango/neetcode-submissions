class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_frequency = defaultdict(int)
        frequency_to_num = defaultdict(list)

        for n in nums:
            num_to_frequency[n] += 1
        
        for key, value in num_to_frequency.items():
            frequency_to_num[value].append(key)

        frequencies = sorted(frequency_to_num.keys(), reverse = True)
        ret = []

        for f in frequencies:
            lst = frequency_to_num.get(f)
            for i in lst:
                ret.append(i)
                if len(ret) == k:
                    return ret

        return ret