class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = []
        def __combine(start, res_set):
            if k == len(res_set):
                result.append(res_set.copy())
                return

            for num in range(start , n + 1):
                res_set.append(num)
                __combine(num + 1, res_set)
                res_set.pop()
        __combine(1, [])
        return result

