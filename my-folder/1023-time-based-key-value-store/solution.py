class TimeMap:

    def __init__(self):
        self.timeMap = {} # dict of str keys mapping to array of tuples (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.timeMap.get(key) is None:
            self.timeMap[key] = [(timestamp, value)]
        else:
            self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        if self.timeMap.get(key) is None:
            return ""

        array = self.timeMap[key] # array of tuples (timestamp, value)

        left = 0
        right = len(array) - 1

        while left <= right:
            middle = (left + right) // 2

            if array[middle][0] < timestamp: # undershot
                left = middle + 1
            elif array[middle][0] > timestamp: # overshot
                right = middle - 1
            else:
                return array[middle][1] # the value if the timestamp matches

        # edge cases
        # at very end
        if array[middle][0] > timestamp and len(array) >= 2 and middle > 0:
            return array[middle - 1][1]
        elif array[middle][0] < timestamp:
            return array[middle][1]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
