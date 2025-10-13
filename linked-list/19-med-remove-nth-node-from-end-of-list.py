# Leetcode 19: Remove Nth Node From End of List
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SolutionLeetcode:
    '''
    Time Complexity: O(L). The algorithm makes two traversal of the list, first to calculate list length L and second to find the (L−n) th node. There are 2L−n operations and time complexity is O(L).
    Space Complexity: O(1)
    '''
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        cur = dummy
        length = 0
        while cur.next:
            cur = cur.next
            length += 1
        
        length = length - n
        cur = dummy
        for _ in range(length):
            cur = cur.next
        
        if cur.next:
            cur.next = cur.next.next
        
        return dummy.next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        # Step 1: Find the length of the linked list
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        # Step 2: If removing the head node
        if n == length:
            return head.next

        # Step 3: Find the node before the one to remove
        cur = head
        for _ in range(length - n - 1):
            cur = cur.next

        # Step 4: Remove the nth node from end
        if cur.next:
            cur.next = cur.next.next

        return head
