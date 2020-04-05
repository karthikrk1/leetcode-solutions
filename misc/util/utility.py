"""
Utility functions
"""

from misc.ds.sll import ListNode

def construct_linked_list(iter):
    """
    Constructs a linked list and returns the head of the node
    Head is assumed to be a dummy value containing the sentinel value as "DUMMY"
    :param iter: List of elements to be constructed as a linked list
    :return: head
    """
    head = ListNode("DUMMY")
    curr = head
    for i in iter:
        new_node = ListNode(i)
        curr.next = new_node
        curr = curr.next
    return head


def print_linked_list(head):
    """
    Prints the linked list. Assumes "head" is a dummy node. Prints from the next value of head
    :param head: Dummy Head node
    :return: None
    """
    curr = head.next
    res = ""
    while curr:
        res += str(curr.val)
        res += ' -> '
        curr = curr.next
    res += "NULL"
    print(res)
