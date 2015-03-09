class Solution(object):
    def max_depth(self, root):
        if root:
            return 1 + max(self.max_depth(root.right), self.max_depth(root.left))
        else:
            return 0

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

if __name__ == "__main__":
    root = TreeNode(0)
    pre = root
    so = Solution()
    root.right = TreeNode(2)
    print so.max_depth(root)
