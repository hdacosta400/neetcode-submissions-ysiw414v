class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums) - 1
        # rotated array is broken into 2 sorted segments
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]: # pivot is in right half
                l = mid + 1
            else:
                r = mid - 1
        pivot = l

    
        def binary_search(l, r):

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        left_half_search = binary_search(0, pivot)
        return left_half_search if left_half_search != -1 else binary_search(pivot , len(nums) - 1)