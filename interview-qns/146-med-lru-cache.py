# Leetcode 146: LRU Cache
# Link: https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashmap = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # Double link the linked list
        self.left.next = self.right
        self.right.prev = self.left
        
    # Remove node from double linked list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    # Add node to the rightmost
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node

        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        node = self.hashmap[key]
        self.remove(node)
        self.insert(node)

        return self.hashmap[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
            self.insert(node)
        else:
            self.hashmap[key] = Node(key, value)
            node = self.hashmap[key]
            self.insert(node)

            if len(self.hashmap) > self.cap:
                lru = self.left.next
                self.remove(lru)
                del self.hashmap[lru.key]
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Alternative solution using OrderedDict (simpler but less educational)
from collections import OrderedDict

class LRUCacheOrderedDict:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key: int) -> int:
        if key in self.cache:
            # Move to end (most recently used)
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing key
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # Remove least recently used (first item)
            self.cache.popitem(last=False)
        
        self.cache[key] = value

# Test cases
if __name__ == "__main__":
    # Test the Node + doubly linked list implementation
    print("Testing LRU Cache with doubly linked list:")
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))      # returns 1
    lru.put(3, 3)          # evicts key 2
    print(lru.get(2))      # returns -1 (not found)
    lru.put(4, 4)          # evicts key 1
    print(lru.get(1))      # returns -1 (not found)
    print(lru.get(3))      # returns 3
    print(lru.get(4))      # returns 4
    
    print("\nTesting LRU Cache with OrderedDict:")
    lru2 = LRUCacheOrderedDict(2)
    lru2.put(1, 1)
    lru2.put(2, 2)
    print(lru2.get(1))     # returns 1
    lru2.put(3, 3)         # evicts key 2
    print(lru2.get(2))     # returns -1 (not found)
    lru2.put(4, 4)         # evicts key 1
    print(lru2.get(1))     # returns -1 (not found)
    print(lru2.get(3))     # returns 3
    print(lru2.get(4))     # returns 4

