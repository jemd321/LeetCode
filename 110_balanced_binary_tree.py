class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BalancedBinaryTree:
    def is_balanced(self, root):
            return self.balanced_subtree(root) != -1

    def balanced_subtree(self, node):
        if not node:
            return 0
        left_height = self.balanced_subtree(node.left)
        right_height = self.balanced_subtree(node.right)

        diff = abs(left_height - right_height)

        if left_height == -1 or right_height == -1 or diff > 1:
            return -1

        return 1 + max(left_height, right_height)




class Test:
    test = BalancedBinaryTree()
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(2)

    p.left.left = TreeNode(3)
    p.left.left.left = TreeNode(7)
    p.left.right = TreeNode(4)

    p.right.left = TreeNode(4)

    print(test.is_balanced(p))