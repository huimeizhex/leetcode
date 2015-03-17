#!/usr/bin/env python
# coding=utf-8


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def swap_pairs(self, head):
        new_head = ListNode(None)
        new_head.next = head
        pre = new_head
        while pre.next and pre.next.next:
            mid = pre.next
            next = mid.next
            pre.next = next
            mid.next = next.next
            next.next = mid
            pre = mid
        return new_head.next

if __name__ == "__main__":
    so = Solution()
    num = raw_input()
    num = num.split()
    head = ListNode(None)
    pre = head
    for val in num:
        pre.next = ListNode(val)
        pre = pre.next
        print val
    head = so.swap_pairs(head.next)
    while head:
        print head.val
        head = head.next
