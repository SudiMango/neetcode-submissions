class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # If target < lastNum, it falls under TRUE which will be to the right
        # If target > lastNum, it falls under FALSE which will be to the left
        # Are target and nums[mid] on the same side

        lastNum = nums[len(nums) - 1]
        res = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            if (target > lastNum and nums[mid] > lastNum) or (target <= lastNum and nums[mid] <= lastNum):
                if target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target <= lastNum and nums[mid] > lastNum:
                    l = mid + 1
                elif target > lastNum and nums[mid] <= lastNum:
                    r = mid - 1

        return res