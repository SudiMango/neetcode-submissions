class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []

        for i, n in enumerate(nums):
            target = 0 - n
            num_to_idx = defaultdict(int)

            for j, k in enumerate(nums):
                if j != i:
                    num_to_idx[k] = j
            
            for j, k in enumerate(nums):
                if j == i:
                    continue

                complement = target - k
                if num_to_idx.get(complement) is not None and num_to_idx.get(complement) != i and num_to_idx.get(complement) != j:
                    to_add = [n, k, nums[num_to_idx.get(complement)]]
                    s = sorted(to_add)
                    if not s in res:
                        res.append(s)

        return res
            

                

