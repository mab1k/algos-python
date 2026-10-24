class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root: TreeNode | None = None

    def insert(self, val) -> None:
        if self.root is None:
            self.root = TreeNode(val)
            return

        node = self.root
        while True:
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(val)
                    return
                node = node.right


def preorder(root: TreeNode | None) -> list:
    result: list = []

    def dfs(node: TreeNode | None) -> None:
        if node is None:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return result


def inorder(root: TreeNode | None) -> list:
    result: list = []

    def dfs(node: TreeNode | None) -> None:
        if node is None:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)

    dfs(root)
    return result


def postorder(root: TreeNode | None) -> list:
    result: list = []

    def dfs(node: TreeNode | None) -> None:
        if node is None:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)

    dfs(root)
    return result


def reverse_preorder(root: TreeNode | None) -> list:
    result: list = []

    def dfs(node: TreeNode | None) -> None:
        if node is None:
            return
        result.append(node.val)
        dfs(node.right)
        dfs(node.left)

    dfs(root)
    return result


def reverse_inorder(root: TreeNode | None) -> list:
    result: list = []

    def dfs(node: TreeNode | None) -> None:
        if node is None:
            return
        dfs(node.right)
        result.append(node.val)
        dfs(node.left)

    dfs(root)
    return result


def reverse_postorder(root: TreeNode | None) -> list:
    result: list = []

    def dfs(node: TreeNode | None) -> None:
        if node is None:
            return
        dfs(node.right)
        dfs(node.left)
        result.append(node.val)

    dfs(root)
    return result
