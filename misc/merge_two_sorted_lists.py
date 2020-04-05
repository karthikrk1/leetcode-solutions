"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

"""

from misc.ds.sll import ListNode

class Solution:
    def merge(self, h1, h2):
        root = ListNode(0)
        merged = root

        while h1 and h2:
            if h1.val <= h2.val:
                merged.next = h1
                h1 = h1.next
            else:
                merged.next = h2
                h2 = h2.next
            merged = merged.next

        if h1:
            merged.next = h1
        if h2:
            merged.next = h2

        return root.next
