class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # every subarray must have at least one element
        l = max(nums) 
        # max assumes no grouping at all
        r = sum(nums)

        def can_split(max_sum: int) -> bool:
            subarrays = 1
            curr_sum = 0

            for num in nums:
                if curr_sum + num <= max_sum:
                    curr_sum += num
                else:
                    subarrays += 1
                    curr_sum = num
                    if subarrays > k:
                        return False

            return True


        while l <= r:
            mid = (l + r) // 2
            if can_split(mid):
                r = mid - 1 # found a valid target sum
            else:
                l = mid + 1
        return l
    
