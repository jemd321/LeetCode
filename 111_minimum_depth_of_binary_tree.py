class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class MinimumDepthOfBinaryTree:
    def minDepth(self, root):
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left and right:
            return 1 + min(left, right)
        if not left or not right:
            return 1 + (left or right)
        return 1

class Test:
    test = MinimumDepthOfBinaryTree()
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(2)

    p.left.left = TreeNode(3)
    p.left.left.left = TreeNode(7)
    p.left.right = TreeNode(4)

    p.right.left = TreeNode(4)

    print(test.minDepth(p))

    q = TreeNode(1)
    q.left = TreeNode(2)
    print(test.minDepth(q))