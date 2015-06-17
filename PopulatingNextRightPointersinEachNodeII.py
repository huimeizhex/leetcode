#!/usr/bin/env python
# coding=utf-8
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution(object):
    def connect(self, root):
        qe = []
        qe.append(root)
        
        while len(qe):
            pre = qe.pop(0)
            if pre is None:
                continue
            if pre.left:
                if pre.right:
                    pre.left.next = pre.right
                else:
                    pre.left.next = self.get_next(pre.next)
            if pre.right:
                pre.right.next = self.get_next(pre.next)
            qe.append(pre.left)
            qe.append(pre.right)
                        
    def get_next(self, root):
        while root:
            #print "left:%s right:%s" %(root.left, root.right)
            print "pre:%s next:%s" %(root.val, root.next)
            if root.left:
                return root.left
            if root.right:
                return root.right
            root = root.next
        return None


def gnerate_binary_tree(num):
    if len(num) == 0:
        return None
    root = TreeNode(num[0])
    i = 1
    q = []
    q.append(root)
    while len(q):
        pre = q.pop(0)
        if i < len(num):
            if num[i] != '#':
                pre.left = TreeNode(num[i])
                i += 1
                q.append(pre.left)
            else:
                i += 1

        if i < len(num):
            if num[i] != '#':
                pre.right = TreeNode(num[i])
                i += 1
                q.append(pre.right)
            else:
                i += 1

    return root

def print_binary_tree(root, res):
    qe = []
    qe.append(root)
    while len(qe):
        pre = qe.pop(0)
        if pre:
            res.append(pre.val)
            if pre.next:
                res.append(pre.next.val)
            else:
                res.append('#')
            qe.append(pre.left)
            qe.append(pre.right)


if __name__ == "__main__":
    num = [2,1,3,0,7,9,1,2,'#',1,0,'#','#',8,8,'#','#','#','#',7]
    root = gnerate_binary_tree(num)
    res = []
    

    so = Solution()
    so.connect(root)

    print_binary_tree(root, res)

    print res

