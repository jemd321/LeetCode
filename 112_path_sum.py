class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class PathSum:
    def hasPathSum(self, root, sum):
        return self.path_sum_helper(root, sum, 0)

    def path_sum_helper(self, node, path_sum, count):
        if not node:
            return False
        count += node.val
        if count == path_sum and not node.left and not node.right:
            return True
        left = self.path_sum_helper(node.left, path_sum, count)
        right = self.path_sum_helper(node.right, path_sum, count)
        return left or right

class Test:
    test = PathSum()

    p = TreeNode(5)

    p.left = TreeNode(4)
    p.right = TreeNode(8)

    p.left.left = TreeNode(11)
    p.left.left.left = TreeNode(7)
    p.left.left.right = TreeNode(2)

    p.right.left = TreeNode(13)
    p.right.right = TreeNode(4)
    p.right.right.right = TreeNode(1)

    print(test.hasPathSum(p, 22))