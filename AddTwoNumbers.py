class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        num = 0
        return self.mySolution(l1, l2, num)

    def mySolution(self, l1, l2, num):
        if l1 is None and l2 is None:
            if num != 0:
                return ListNode(num)
            else:
                return None
        mid = l1 if l1 else l2
        if l1:
            num += l1.val
            l1 = l1.next
        if l2:
            num += l2.val
            l2 = l2.next
        mid.val = num%10
        mid.next = self.mySolution(l1, l2, num/10)
        return mid

def convertStringListNode(string):
    head = ListNode(0)
    pre = head
    for chr in string:
        val = int(chr)
        pre.next = ListNode(val)
        pre = pre.next
    return head.next

def printList(linklist):
    while linklist:
        print "%d "  %linklist.val,
        linklist = linklist.next



if __name__ == '__main__':
    so = Solution()
    l1 = raw_input()
    l2 = raw_input()
    l1 = convertStringListNode(l1)
    l2 = convertStringListNode(l2)
    res = so.addTwoNumbers(l1, l2)
    printList(res)

