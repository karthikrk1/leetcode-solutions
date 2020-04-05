"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

from misc.ds.sll import ListNode

class Solution:
    def add_two_numbers(self, h1, h2):
        node = ListNode(-1)
        self.sum(h1, h2, 0, node)
        return node

    def sum(self, h1, h2, carry, node):
        total = h1.val + h2.val + carry

        carry = 0
        if total >= 10:
            total -= 10
            carry = 1

        node.val = total
        newNode = ListNode(-1)
        node.next = newNode

        if h1.next and h2.next:
            self.sum(h1.next, h2.next, carry, newNode)
        elif h1.next:
            self.sum(h1.next, ListNode(0), carry, newNode)
        elif h2.next:
            self.sum(ListNode(0), h2.next, carry, newNode)
        else:
            if carry > 0:
                node.next.val = carry
            else:
                node.next = None
