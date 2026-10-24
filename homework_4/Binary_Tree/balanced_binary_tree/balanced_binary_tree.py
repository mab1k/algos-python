class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root: TreeNode | None) -> bool:
    def height_or_unbalanced(node: TreeNode | None) -> int:
        if node is None:
            return 0

        left_h = height_or_unbalanced(node.left)
        if left_h == -1:
            return -1

        right_h = height_or_unbalanced(node.right)
        if right_h == -1:
            return -1

        if abs(left_h - right_h) > 1:
            return -1

        return 1 + max(left_h, right_h)

    return height_or_unbalanced(root) != -1
