class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class LowestCommonAncestorOfABinarySearchTree:
    def lowestCommonAncestor(self, root, p, q):
        if not root or not p and not q:
            return None
        if p.val == q.val:
            return p
        return self.lca_helper(root, p, q)

    def lca_helper(self, root, p, q):
        n = root.val
        if p.val < n < q.val or p.val > n > q.val:
            return root
        if p.val == n:
            return p
        if q.val == n:
            return q
        if p.val < n and q.val < n:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > n and q.val > n:
            return self.lowestCommonAncestor(root.right, p, q)


class Test:
    test = LowestCommonAncestorOfABinarySearchTree()

    root = TreeNode(6)
    root.left = TreeNode(2)

    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)

    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    root.right = TreeNode(8)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    result = test.lowestCommonAncestor(root, TreeNode(3), TreeNode(5))
    print(result.val) if result else print(result)

    result = test.lowestCommonAncestor(root, TreeNode(4), TreeNode(5))
    print(result.val) if result else print(result)

    result = test.lowestCommonAncestor(root, TreeNode(2), TreeNode(8))
    print(result.val) if result else print(result)

    result = test.lowestCommonAncestor(root, TreeNode(0), TreeNode(6))
    print(result.val) if result else print(result)

    result = test.lowestCommonAncestor(root, TreeNode(8), TreeNode(8))
    print(result.val) if result else print(result)

    result = test.lowestCommonAncestor(root, TreeNode(6), TreeNode(6))
    print(result.val) if result else print(result)

