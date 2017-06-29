class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class InvertBinaryTree:
    def invertTree(self, root):
        if not root:
            return None
        left = root.left
        right = root.right
        root.left = self.invertTree(right)
        root.right = self.invertTree(left)
        return root


class Test:
    test = InvertBinaryTree()

    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    p.left.left = TreeNode(4)
    p.left.right = TreeNode(5)

    p.right.left = TreeNode(6)
    p.right.right = TreeNode(7)

    root = test.invertTree(p)
    print(root)
