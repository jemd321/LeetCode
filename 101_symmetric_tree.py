class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SymmetricTree:
    def is_symmetric(self, root):
        if root is None:
            return True
        return self.compare_symmetry(root.left, root.right)

    def compare_symmetry(self ,left, right):
        if not left or not right:
            return left is None and right is None
        if left.val != right.val:
            return False
        return self.compare_symmetry(left.left, right.right) and self.compare_symmetry(left.right, right.left)

class Test:
    test = SymmetricTree()

    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(2)

    p.left.left = TreeNode(3)
    p.left.right = TreeNode(4)

    p.right.left = TreeNode(4)
    p.right.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(2)

    q.left.right = TreeNode(3)

    q.right.left = TreeNode(3)
    q.right.right = TreeNode(3)

    print(test.is_symmetric(p))
    print(test.is_symmetric(q))
