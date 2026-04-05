import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time_to_eat_all(k):
            return sum(math.ceil(pile / k) for pile in piles)

        lower = 1
        upper = max(piles)

        while lower != upper:

            k = (lower + upper) // 2
            consumption_time = time_to_eat_all(k)

            if consumption_time > h:
                lower = k + 1
            else:
                upper = k
        return lower
    





        