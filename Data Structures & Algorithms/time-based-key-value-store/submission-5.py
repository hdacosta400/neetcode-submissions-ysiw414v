class TimeMap:

    def __init__(self):
        # map key to [ (value, timestamp) ]
        self.time_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""

        arr = self.time_map[key]
        l, r = 0, len(arr) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            mid_val, mid_time = arr[mid]

            if mid_time <= timestamp:
                res = mid_val        # valid candidate
                l = mid + 1          # try to find a newer one
            else:
                r = mid - 1

        return res


