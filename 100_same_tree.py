class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SameTree:
    def is_same_tree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        # Left Branch
        if p.left and q.left:
            left_same = self.is_same_tree(p.left, q.left)
        elif not p.left and not q.left:
            left_same = True
        else:
            left_same = False

        # Right Branch
        if p.right and q.right:
            right_same = self.is_same_tree(p.right, q.right)
        elif not p.right and not q.right:
            right_same = True
        else:
            right_same = False

        return left_same and right_same

class Test:
    test = SameTree()

    p = TreeNode(5)
    p.left = TreeNode(3)
    p.right = TreeNode(7)

    p.left.left = TreeNode(1)
    p.left.right = TreeNode(2)

    p.right.left = TreeNode(6)
    p.right.right = TreeNode(8)

    q = TreeNode(5)
    q.left = TreeNode(3)
    q.right = TreeNode(7)

    q.left.left = TreeNode(1)
    q.left.right = TreeNode(2)

    q.right.left = TreeNode(6)
    q.right.right = TreeNode(9)

    print(test.is_same_tree(p, q))


