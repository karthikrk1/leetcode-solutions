"""
Reverse a singly linked list.
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

from misc.util.utility import construct_linked_list


class Solution:
    def reverse_iter(self, head):
        prev = next = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head


def main():
    sol = Solution()
    head = construct_linked_list([1,2,3,4,5])
    node = sol.reverse_iter(head)
    assert node.val == 5


if __name__ == '__main__':
    main()
