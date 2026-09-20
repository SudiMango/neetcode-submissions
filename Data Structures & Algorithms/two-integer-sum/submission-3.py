class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = defaultdict(int)

        for i, n in enumerate(nums):
            num_to_index[n] = i
        
        for i, n in enumerate(nums):
            new_target = target - n
            if new_target in num_to_index and i is not num_to_index[new_target]:
                return [i, num_to_index[new_target]]

        return []