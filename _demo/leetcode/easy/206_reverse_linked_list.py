# Recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        node = head
        
        if (node == None):
            return node

        if (node.next == None):
            return node

        last = self.reverseList(node.next)
        node.next.next = node
        node.next = None
        return last