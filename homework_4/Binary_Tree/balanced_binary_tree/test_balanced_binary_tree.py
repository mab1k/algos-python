from balanced_binary_tree import TreeNode, is_balanced


def test_empty_tree():
    # граница: пустое дерево сбалансировано
    assert is_balanced(None) is True


def test_single_node():
    # граница: один узел
    assert is_balanced(TreeNode(1)) is True


def test_two_nodes_left():
    # граница: корень + левый ребёнок — разница высот 1
    #     2
    #    /
    #   1
    assert is_balanced(TreeNode(2, TreeNode(1))) is True


def test_two_nodes_right():
    # граница: корень + правый ребёнок
    #   1
    #    \
    #     2
    assert is_balanced(TreeNode(1, None, TreeNode(2))) is True


def test_perfect_small():
    # типичный: идеально сбалансированное
    #       2
    #      / \
    #     1   3
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert is_balanced(root) is True


def test_balanced_height_diff_one():
    # типичный: у корня |hl - hr| = 1, оба поддерева сбалансированы
    #         3
    #        / \
    #       2   4
    #      /
    #     1
    root = TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4))
    assert is_balanced(root) is True


def test_unbalanced_left_heavy():
    # типичный: левая цепочка длины 2 при пустом правом — у корня diff = 2
    #     3
    #    /
    #   2
    #  /
    # 1
    root = TreeNode(3, TreeNode(2, TreeNode(1)))
    assert is_balanced(root) is False


def test_unbalanced_right_heavy():
    # типичный: правая цепочка
    #   1
    #    \
    #     2
    #      \
    #       3
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert is_balanced(root) is False


def test_unbalanced_deep_not_at_root():
    # нетривиальный: корень выглядит ок, дисбаланс глубже
    #           4
    #          / \
    #         3   5
    #        /
    #       2
    #      /
    #     1
    # У узла 3: left height=2, right=0 → |2-0|=2 → False
    root = TreeNode(4, TreeNode(3, TreeNode(2, TreeNode(1))), TreeNode(5))
    assert is_balanced(root) is False


def test_balanced_larger():
    # нетривиальный: полное дерево высоты 3
    #            4
    #         /     \
    #        2       6
    #       / \     / \
    #      1   3   5   7
    root = TreeNode(
        4,
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(6, TreeNode(5), TreeNode(7)),
    )
    assert is_balanced(root) is True


def test_balanced_almost_complete():
    # нетривиальный: почти полное, разница высот ≤ 1 везде
    #            4
    #         /     \
    #        2       6
    #       / \     /
    #      1   3   5
    root = TreeNode(
        4,
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(6, TreeNode(5)),
    )
    assert is_balanced(root) is True


def test_unbalanced_both_sides_deep():
    # нетривиальный: оба поддерева «глубокие», но одно сильно глубже
    #              5
    #            /   \
    #           3     7
    #          /     / \
    #         2     6   8
    #        /
    #       1
    # У узла 3: left=2, right=0 → False
    root = TreeNode(
        5,
        TreeNode(3, TreeNode(2, TreeNode(1))),
        TreeNode(7, TreeNode(6), TreeNode(8)),
    )
    assert is_balanced(root) is False


def test_three_level_left_ok():
    # граница: высота слева 2, справа 1 — ещё допустимо
    #         4
    #        / \
    #       2   5
    #      / \
    #     1   3
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
    assert is_balanced(root) is True
