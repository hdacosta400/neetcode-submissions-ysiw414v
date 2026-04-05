class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        stored_values = self.store[key]

        left = 0
        right = len(stored_values) - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2

            if stored_values[mid][1] <= timestamp:
                res = stored_values[mid][0]
                left = mid + 1 # search later times
            else:
                right = mid - 1 # search earlier times
        return res




        
