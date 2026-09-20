class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        num_zeros = 0

        res = 1
        for n in nums:
            if n == 0:
                num_zeros += 1
                continue
            
            res *= n

        if num_zeros > 1:
            return [0 for _ in range(len(nums))]

        for n in nums:
            if n == 0:
                ret.append(int(res))
            else:
                if num_zeros != 0:
                    ret.append(0)
                else:
                    ret.append(int(res/n))
                    
            

        return ret