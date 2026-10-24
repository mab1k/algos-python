from validate_bst import TreeNode, is_valid_bst


def test_empty_tree():
    # граница: пустое дерево — валидный BST
    assert is_valid_bst(None) is True


def test_single_node():
    # граница: один узел
    assert is_valid_bst(TreeNode(1)) is True


def test_valid_balanced():
    # типичный: корректный BST
    #       2
    #      / \
    #     1   3
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert is_valid_bst(root) is True


def test_invalid_simple():
    # типичный: нарушен порядок у корня
    #       1
    #      / \
    #     2   3
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert is_valid_bst(root) is False


def test_invalid_deep_violation():
    # нетривиальный: локально похоже на BST, но нарушен глобальный инвариант
    #         5
    #        / \
    #       1   4
    #          / \
    #         3   6
    # 4 < 5, но 3 должно быть < 5 и > 4 — 3 < 4, ok локально у 4,
    # однако правое поддерево корня целиком должно быть > 5, а 3 и 4 — нет.
    root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert is_valid_bst(root) is False


def test_invalid_left_grandchild_too_large():
    # нетривиальный: правый потомок левого ребёнка ≥ корня
    #         10
    #        /
    #       5
    #        \
    #         12   ← 12 > 10, но лежит в левом поддереве
    root = TreeNode(10, TreeNode(5, None, TreeNode(12)))
    assert is_valid_bst(root) is False


def test_invalid_right_grandchild_too_small():
    # нетривиальный: левый потомок правого ребёнка ≤ корня
    #         10
    #           \
    #            15
    #           /
    #          8    ← 8 < 10, но лежит в правом поддереве
    root = TreeNode(10, None, TreeNode(15, TreeNode(8)))
    assert is_valid_bst(root) is False


def test_valid_skewed_left():
    # граница: вырожденное влево (строго убывающая цепочка)
    #      3
    #    /
    #   2
    #  /
    # 1
    root = TreeNode(3, TreeNode(2, TreeNode(1)))
    assert is_valid_bst(root) is True


def test_valid_skewed_right():
    # граница: вырожденное вправо
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert is_valid_bst(root) is True


def test_duplicates_not_allowed():
    # граница: равные значения нарушают строгий BST (low < val < high)
    #       2
    #      /
    #     2
    root = TreeNode(2, TreeNode(2))
    assert is_valid_bst(root) is False


def test_negatives():
    # типичный: отрицательные значения, валидный BST
    #        0
    #       / \
    #     -2   1
    #     /
    #   -3
    root = TreeNode(0, TreeNode(-2, TreeNode(-3)), TreeNode(1))
    assert is_valid_bst(root) is True


def test_only_left_valid():
    # граница: только левое поддерево
    root = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)))
    assert is_valid_bst(root) is True


def test_valid_larger():
    # нетривиальный: более крупное корректное дерево
    #           8
    #         /   \
    #        3     10
    #       / \      \
    #      1   6      14
    #         / \    /
    #        4   7  13
    root = TreeNode(
        8,
        TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))),
        TreeNode(10, None, TreeNode(14, TreeNode(13))),
    )
    assert is_valid_bst(root) is True
