class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1
        upper = max(piles)


        min_rate = upper
        while lower <= upper:
            k = (lower + upper) // 2
            hours = 0
            for p in piles: # use guess to compute heuristiic
                hours += math.ceil(p / k)
            if hours <= h:
                min_rate = min(min_rate, k)
                upper = k - 1 # try to eat slower 
            else:
                lower = k + 1 # need to eat faster
        return min_rate
