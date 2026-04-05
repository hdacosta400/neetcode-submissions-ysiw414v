class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1

        while lower <= upper:
            guess = lower + (upper - lower) // 2
            if nums[guess] == target:
                return guess
            elif nums[guess] < target:
                lower = guess + 1
            else:
                upper = guess - 1
        return lower