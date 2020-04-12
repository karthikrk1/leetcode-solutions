"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
"""
from misc.ds.sll import ListNode
import itertools

class Solution:
    def add_two_numbers_with_msb_first(self, l1, l2):
        def it(node):
            if node:
                yield from it(node.next)
                yield node.val

            ans = ListNode(-1)
            carry = 0
            for v1, v2 in itertools.zip_longest(it(l1), it(l2), fillvalue=0):
                sum = v1 + v2 +  carry
                val, carry = ListNode(sum%10), sum//10
                val.next, ans.next = ans.next, val

            if carry > 0:
                val = ListNode(carry)
                val.next, ans.next = ans.next, val
            return ans.next
