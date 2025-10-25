# Leetcode 143: Reorder List
# Link: https://leetcode.com/problems/reorder-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    '''
    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        # Find the middle of linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Revert the second part of linked list
        prev, cur = None, slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxty
        
        # Merge two sorted linked list
        first, second = head, prev
        while second.next:
            tmp1 = first.next
            first.next = second
            first = tmp1

            tmp2 = second.next
            second.next = first
            second = tmp2