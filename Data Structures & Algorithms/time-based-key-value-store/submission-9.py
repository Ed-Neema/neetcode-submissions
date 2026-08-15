class TimeMap:

    def __init__(self):
        self.dictionary = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append([value,timestamp])

        

    def get(self, key: str, timestamp: int) -> str:
        #I'll have to binary search the list of values for the right timestamp
        #if I don't find it, I'll just return the [-1]'s timestamp
        # [[val, time], [val, time],[val, time]]
        l,r = 0, len(self.dictionary[key]) - 1
        
        while l <= r:
            mid = (l+r) // 2
            if self.dictionary[key][mid][1] == timestamp:
                return  self.dictionary[key][mid][0]
            elif timestamp > self.dictionary[key][mid][1]:
                l = mid + 1
            else:
                r = mid - 1
        #if we don't return from the binary search, then there's no value at that timestamp
        # if list is not empty:
            # if the earliest value is larger than timestamp, then just return ""
            # else, return the previous value closest to timestamp, which is being tracked by r
        #f list is empty return ""
        if len(self.dictionary[key]) != 0:
            if self.dictionary[key][0][1] > timestamp:
                return ""
            else: 
                return self.dictionary[key][r][0]
        
        return ""
        
