#!/usr/bin/env python
# coding=utf-8
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def merge_two_list(self, l1, l2):
        head = l1
        pre = None
        while l1 and l2:
            if l2.val <= l1.val:
                if pre is None:
                    mid = l2.next
                    l2.next = l1
                    pre = l2
                    head = l2 
                    l2 = mid
                else:
                    mid = l2.next
                    pre.next = l2
                    l2.next = l1
                    l2 = mid
                    pre = pre.next
            else:
                pre = l1
                l1 = l1.next
        if l1 is None:
            if pre:
                pre.next = l2
            else:
                return l2
        return head

def get_list(num):
    l1 = None
    head = None
    for i in num:
        if l1:
            l1.next = ListNode(i)
            l1 = l1.next
        else:
            l1 = ListNode(i)
            head = l1
    return head

if __name__ == "__main__":
    so = Solution()
    num1 = [3]
    num2 = []
    l1 = get_list(num1)
    l2 = get_list(num2)
    res = so.merge_two_list(l1, l2)
    while res:
        print res.val
        res = res.next
