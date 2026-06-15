class TimeMap:

    def __init__(self):
        self.vals = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.vals:
            self.vals[key] = []
        self.vals[key].append((timestamp, value))
        
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.vals.get(key)
        if values is None:
            return ""

        l, r = 0, len(values) - 1
        best_ans = ""

        while l <= r:
            m = l + (r - l) // 2

            if values[m][0] == timestamp:
                return values[m][1]
            elif values[m][0] < timestamp:
                best_ans = values[m][1]
                l = m + 1
            else:
                r = m - 1
        return best_ans
        
