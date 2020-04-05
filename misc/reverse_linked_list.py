"""
Reverse a singly linked list.
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

from misc.ds.sll import ListNode
from misc.util.utility import construct_linked_list, print_linked_list


class Solution:
    def reverse(self, head):
        return None


def main():
    sol = Solution()
    head = construct_linked_list([1,2,3,4,5])
    print_linked_list(head)
    #node = sol.reverse(head)
    #assert node.next.val == 5


if __name__ == '__main__':
    main()
