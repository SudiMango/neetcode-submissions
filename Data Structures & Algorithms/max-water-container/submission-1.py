class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        total_max = (r - l) * min(heights[l], heights[r])

        while l < r:
            curr = (r - l) * min(heights[l], heights[r])
            if curr > total_max:
                total_max = curr
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return total_max