"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""
from misc.ds.sll import ListNode

class Solution():
    def merge_k_sorted_lists(self, lists):
        d = {}
        for l in lists:
            curr = l
            while curr:
                if curr.val in d:
                    d[curr.val] += 1
                else:
                    d[curr.val] = 1

        head = ListNode(-1)
        result = head
        for key, val in (sorted(d.items(), key = lambda x: x[0])):
            for x in range(0, val):
                result.next = ListNode(key)
                result = result.next
        return head.next
