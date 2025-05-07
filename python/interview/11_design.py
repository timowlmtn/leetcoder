"""
DESIGN INTERVIEW CHEAT SHEET

General Steps:
1. Clarify Requirements
   • What operations? (e.g. push/pop/getMin)
   • Constraints: max size, thread-safe, memory limits
   • Performance targets: average vs worst-case, big-O for each API

2. Outline Approach
   • Data structures: arrays, linked lists, hash tables, heaps, trees, deque
   • Trade-offs: time vs space, simplicity vs extensibility

3. Define API
   • Write method signatures & class name
   • Describe inputs/outputs and error handling

4. Sketch Implementation
   • Pseudocode or high-level comments
   • Identify core helper functions

5. Code & Test
   • Implement each method
   • Think edge-cases (empty state, overflow, duplicates)
   • Verify complexity

-------------------------------------------------------------------------------
"""

"""
#1. MinStack
# Supports push, pop, top, getMin in O(1) time
"""


class MinStack:
    def __init__(self):
        # main stack holds (value, current_min)
        self.stack = []
        # Complexity: O(1) init, space O(n)

    def push(self, x: int) -> None:
        # Compute new min so far
        current_min = x if not self.stack else min(x, self.stack[-1][1])
        self.stack.append((x, current_min))
        # Time: O(1)

    def pop(self) -> None:
        if not self.stack:
            raise IndexError("pop from empty stack")
        self.stack.pop()
        # Time: O(1)

    def top(self) -> int:
        if not self.stack:
            raise IndexError("top from empty stack")
        return self.stack[-1][0]
        # Time: O(1)

    def getMin(self) -> int:
        if not self.stack:
            raise IndexError("getMin from empty stack")
        return self.stack[-1][1]
        # Time: O(1)


"""-------------------------------------------------------------------------------

#2. LRUCache
# Capacity-bounded cache, get and put in O(1) average time
"""
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # OrderedDict keeps insertion order; move_to_end updates recency
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # mark as recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update and mark recent
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # pop oldest item
            self.cache.popitem(last=False)


"""
# Complexity: O(1) amortized for get/put, space O(capacity)

-------------------------------------------------------------------------------

#3. Design HashSet
# Implement HashSet without built-ins; handle collisions with chaining
"""


class MyHashSet:
    def __init__(self, bucket_size: int = 10000):
        self.bucket_size = bucket_size
        self.buckets = [[] for _ in range(bucket_size)]

    def _bucket_index(self, key: int) -> int:
        return key % self.bucket_size

    def add(self, key: int) -> None:
        idx = self._bucket_index(key)
        if key not in self.buckets[idx]:
            self.buckets[idx].append(key)

    def remove(self, key: int) -> None:
        idx = self._bucket_index(key)
        bucket = self.buckets[idx]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.buckets[self._bucket_index(key)]


"""
# Time: O(1) avg, O(n) worst-case; choose bucket_size wisely to minimize collisions

-------------------------------------------------------------------------------

#4. ParkingSystem
# Fixed capacities for car sizes; simple counters
"""


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.capacity = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        # carType: 1=big, 2=medium, 3=small
        if self.capacity.get(carType, 0) > 0:
            self.capacity[carType] -= 1
            return True
        return False


# Time & Space: O(1)

"""
-------------------------------------------------------------------------------

# GENERIC DESIGN TIPS:

# • Always ask:
#   – “What if the load is very high? Does it need sharding?”
#   – “Should operations be thread-safe? Use locks or concurrent DS?”
#   – “What about persistence? Write-through vs write-back?”
#   – “Cleanup: do we need TTL or eviction policies?”

# • Mention trade-offs:
#   – Simplicity vs performance: built-ins vs custom
#   – Memory overhead of extra pointers/indices
#   – Amortized vs worst-case time

# • Complexity summary:
#   – State operation by operation: “push: O(1), pop: O(1), space: O(n)”
#   – Best/worst/average scenarios

# • Testing & edge cases:
#   – empty structures, null/invalid inputs
#   – capacity boundaries, overflow/underflow

# • Follow-up discussion:
#   – How to extend to support additional ops?
#   – Scaling to distributed environment?
"""

# End of cheat-sheet module.
