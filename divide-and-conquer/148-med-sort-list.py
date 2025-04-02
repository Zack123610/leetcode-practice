# Leetcode 148: Sort List
# Link: https://leetcode.com/problems/sort-list/
# Medium
# Tags: Linked List, Sorting, Divide and Conquer

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
            
        # Find middle of the linked list
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        # Split the list into two halves
        second_half = slow.next
        slow.next = None
        
        # Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(second_half)
        
        # Merge the sorted halves
        return self.merge(left, right)
    
    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        
        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
            
        # Attach remaining nodes
        if left:
            current.next = left
        if right:
            current.next = right
            
        return dummy.next

# Example usage:
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
