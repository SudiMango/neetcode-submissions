class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_to_idx = defaultdict(int)

        for i, v in enumerate(numbers):
            num_to_idx[v] = i + 1

        for i, v in enumerate(numbers):
            complement = target - v

            if num_to_idx.get(complement):
                idx1 = i + 1
                idx2 = num_to_idx.get(complement)
                if idx1 < idx2:
                    return [idx1, idx2]
                else:
                    return [idx2, idx1]

        