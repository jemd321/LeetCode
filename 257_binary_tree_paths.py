class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTreePaths:
    def __init__(self):
        self.paths = []

    def binaryTreePaths(self, root):
        if not root:
            return self.paths
        if self.is_leaf_node(root):
            self.paths.append(str(root.val))
        self.path_helper(root.left, str(root.val))
        self.path_helper(root.right, str(root.val))
        return self.paths

    def path_helper(self, node, path):
        if not node:
            return
        sub_path = "->" + str(node.val)
        path += sub_path

        # Is leaf node
        if self.is_leaf_node(node):
            self.paths.append(path)
            return
        self.path_helper(node.left, path)
        self.path_helper(node.right, path)

    def is_leaf_node(self, node):
        return not node.left and not node.right


class Test:
    test = BinaryTreePaths()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)

    print(test.binaryTreePaths(root))
