class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lower = 0
        upper = len(nums) - 1
        
        while lower <= upper:
            guess = (lower + upper) // 2
            print(lower, upper, guess)
            if nums[guess] == target:
                return guess
            if nums[guess] < target:
                lower = guess + 1
            else:
                upper = guess - 1
        return -1
        