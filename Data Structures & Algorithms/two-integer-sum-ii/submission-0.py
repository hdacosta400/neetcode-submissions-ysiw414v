class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        first = 0
        last = len(numbers) - 1

        while first != last:
            curr_sum = numbers[first] + numbers[last]

            if curr_sum == target:
                return [first + 1, last + 1]
            elif curr_sum < target:
                first += 1
            elif curr_sum > target:
                last -= 1
        return None
        