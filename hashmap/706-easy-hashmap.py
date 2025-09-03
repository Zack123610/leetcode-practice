# Leetcode 706: Design HashMap
# Link: https://leetcode.com/problems/design-hashmap/

class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for i in range(1000)]

    def hash(self, key):
        return key%len(self.map)
        
    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        prev = self.map[index]
        curr = prev.next

        while curr:
            if curr.key == key:
                curr.val = value
                return
            prev = curr
            curr = curr.next

        prev.next = ListNode(key, value)
        

    def get(self, key: int) -> int:
        index = self.hash(key)
        curr = self.map[index].next

        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        
        return -1
        
    def remove(self, key: int) -> None:
        index = self.hash(key)
        curr = self.map[index]

        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next