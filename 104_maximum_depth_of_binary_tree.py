class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class MaximumDepthOfBinaryTree:
    def maximum_depth(self, root):
        if not root:
            return 0
        max_depth = 1 + max((self.maximum_depth(root.left), self.maximum_depth(root.right)))
        return max_depth


class Test:
    test = MaximumDepthOfBinaryTree()
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(2)

    p.left.left = TreeNode(3)
    p.left.left.left = TreeNode(7)
    p.left.right = TreeNode(4)

    p.right.left = TreeNode(4)


    print(test.maximum_depth(p))


    