class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_to_idx = defaultdict(int)

        for i, n in enumerate(numbers):
            num_to_idx[n] = i

        for i, n in enumerate(numbers):
            complement = target - n
            
            found = num_to_idx.get(complement)
            if found:
                if i < found:
                    return [i + 1, found + 1]
                else:
                    return [found + 1, i + 1]
