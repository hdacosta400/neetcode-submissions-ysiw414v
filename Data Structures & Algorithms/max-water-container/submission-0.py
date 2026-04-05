class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        get_capacity = lambda l,r : (r - l) * min(heights[l], heights[r])

        max_seen = get_capacity(left, right)

        while left < right:
            capacity = get_capacity(left, right)

            if capacity > max_seen:
                max_seen = capacity

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_seen
            



        