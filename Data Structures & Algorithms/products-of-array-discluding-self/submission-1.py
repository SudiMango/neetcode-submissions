class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_zeros = 0
        total_mult = 1
        for n in nums:
            if n == 0:
                num_zeros += 1

        ret = []

        if num_zeros > 1:
            for i in range(len(nums)):
                ret.append(0)
            return ret

        if num_zeros == 1:
            for n  in nums:
                if n != 0:
                    total_mult *= n
            
            for i, v in enumerate(nums):
                if v == 0:
                    ret.append(total_mult)
                else:
                    ret.append(0)

            return ret

        if num_zeros == 0:
            for n  in nums:
                    total_mult *= n
        
            for i, v in enumerate(nums):
                ret.append(int(total_mult / nums[i]))

        return ret