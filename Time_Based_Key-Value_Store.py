# Implement a time-based key-value data structure that supports:

# Storing multiple values for the same key at specified time stamps
# Retrieving the key's value at a specified timestamp
# Implement the TimeMap class:

# TimeMap() Initializes the object.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns the most recent value of key if set was previously called on it and the most recent timestamp for that key prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp). If there are no values, it returns "".
# Note: For all calls to set, the timestamps are in strictly increasing order.

# Example 1:

# Input:
# ["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]

# Output:
# [null, null, "happy", "happy", null, "sad"]

# Explanation:
# TimeMap timeMap = new TimeMap();
# timeMap.set("alice", "happy", 1);  // store the key "alice" and value "happy" along with timestamp = 1.
# timeMap.get("alice", 1);           // return "happy"
# timeMap.get("alice", 2);           // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
# timeMap.set("alice", "sad", 3);    // store the key "alice" and value "sad" along with timestamp = 3.
# timeMap.get("alice", 3);           // return "sad"

class TimeMap:
    def __init__(self):
        from collections import defaultdict
        self.mapper = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapper[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.mapper[key]) - 1
        res = ''
        while left <= right:
            mid = (left + right) // 2
            if self.mapper[key][mid][0] <= timestamp:
                res = self.mapper[key][left][1]
                left = mid + 1
            else:
                right = mid - 1
        return res

if __name__=='__main__':
    timeMap = TimeMap()
    print(timeMap.set("alice", "happy", 1)) # // store the key "alice" and value "happy" along with timestamp = 1.
    print(timeMap.get("alice", 1)) #         // return "happy"
    print(timeMap.get("alice", 2)) #           // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
    print(timeMap.set("alice", "sad", 3)) #  // store the key "alice" and value "sad" along with timestamp = 3.
    print(timeMap.get("alice", 3))        # // return "sad"


        
