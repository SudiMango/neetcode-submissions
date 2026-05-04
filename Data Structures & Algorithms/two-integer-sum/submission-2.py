class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = defaultdict(int)

        for i, v in enumerate(nums):
            num_to_index[v] = i

        for i, v in enumerate(nums):
            complement = target - v

            found_complement = num_to_index.get(complement, -1)
            if found_complement != -1 and found_complement != i:
                return [i, found_complement]

        