class Solution:
    def findMin(self, nums: List[int]) -> int:
        lastNum = nums[len(nums) - 1]

        l, r = 0, len(nums) - 1
        lastMinNum = -1001
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > lastNum:
                l = mid + 1
            else:
                lastMinNum = nums[mid]
                r = mid - 1

        return lastMinNum