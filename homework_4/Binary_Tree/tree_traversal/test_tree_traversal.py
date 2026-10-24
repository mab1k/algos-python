from tree_traversal import (
    BST,
    TreeNode,
    inorder,
    postorder,
    preorder,
    reverse_inorder,
    reverse_postorder,
    reverse_preorder,
)


def _build_bst(values: list) -> TreeNode | None:
    tree = BST()
    for v in values:
        tree.insert(v)
    return tree.root


def test_empty_tree_traversals():
    assert preorder(None) == []
    assert inorder(None) == []
    assert postorder(None) == []
    assert reverse_preorder(None) == []
    assert reverse_inorder(None) == []
    assert reverse_postorder(None) == []


def test_single_node():
    # граница: один узел
    root = TreeNode(42)
    for walk in (
        preorder,
        inorder,
        postorder,
        reverse_preorder,
        reverse_inorder,
        reverse_postorder,
    ):
        assert walk(root) == [42]


def test_insert_builds_bst():
    # типичный: вставка сохраняет BST, inorder возрастает
    root = _build_bst([5, 3, 7, 2, 4, 6, 8])
    assert inorder(root) == [2, 3, 4, 5, 6, 7, 8]


def test_insert_duplicates_go_right():
    # граница: равные значения идут вправо
    root = _build_bst([2, 2, 2])
    assert root.val == 2
    assert root.left is None
    assert root.right is not None and root.right.val == 2
    assert inorder(root) == [2, 2, 2]


def test_six_traversals_on_bst():
    # типичный: дерево
    #       4
    #      / \
    #     2   6
    #    / \ / \
    #   1  3 5  7
    root = _build_bst([4, 2, 6, 1, 3, 5, 7])

    assert preorder(root) == [4, 2, 1, 3, 6, 5, 7]
    assert inorder(root) == [1, 2, 3, 4, 5, 6, 7]
    assert postorder(root) == [1, 3, 2, 5, 7, 6, 4]
    assert reverse_preorder(root) == [4, 6, 7, 5, 2, 3, 1]
    assert reverse_inorder(root) == [7, 6, 5, 4, 3, 2, 1]
    assert reverse_postorder(root) == [7, 5, 6, 3, 1, 2, 4]


def test_skewed_left():
    # граница: вырожденное дерево влево (убывающая вставка)
    root = _build_bst([5, 4, 3, 2, 1])
    assert preorder(root) == [5, 4, 3, 2, 1]
    assert inorder(root) == [1, 2, 3, 4, 5]
    assert postorder(root) == [1, 2, 3, 4, 5]
    assert reverse_inorder(root) == [5, 4, 3, 2, 1]


def test_skewed_right():
    # граница: вырожденное дерево вправо (возрастающая вставка)
    root = _build_bst([1, 2, 3, 4, 5])
    assert preorder(root) == [1, 2, 3, 4, 5]
    assert inorder(root) == [1, 2, 3, 4, 5]
    assert postorder(root) == [5, 4, 3, 2, 1]


def test_only_left_child():
    # граница: корень только с левым ребёнком
    root = TreeNode(2, left=TreeNode(1))
    assert preorder(root) == [2, 1]
    assert inorder(root) == [1, 2]
    assert postorder(root) == [1, 2]
    assert reverse_preorder(root) == [2, 1]
    assert reverse_inorder(root) == [2, 1]
    assert reverse_postorder(root) == [1, 2]


def test_only_right_child():
    # граница: корень только с правым ребёнком
    root = TreeNode(1, right=TreeNode(2))
    assert preorder(root) == [1, 2]
    assert inorder(root) == [1, 2]
    assert postorder(root) == [2, 1]
    assert reverse_preorder(root) == [1, 2]
    assert reverse_inorder(root) == [2, 1]
    assert reverse_postorder(root) == [2, 1]


def test_nontrivial_unbalanced_shape():
    # нетривиальный: несбалансированная форма BST
    #         10
    #        /  \
    #       5    15
    #      / \     \
    #     3   7     20
    #        /
    #       6
    root = _build_bst([10, 5, 15, 3, 7, 20, 6])
    assert inorder(root) == [3, 5, 6, 7, 10, 15, 20]
    assert preorder(root) == [10, 5, 3, 7, 6, 15, 20]
    assert postorder(root) == [3, 6, 7, 5, 20, 15, 10]
    assert reverse_preorder(root) == [10, 15, 20, 5, 7, 6, 3]
    assert reverse_inorder(root) == [20, 15, 10, 7, 6, 5, 3]
    assert reverse_postorder(root) == [20, 15, 6, 7, 3, 5, 10]


def test_negatives_and_zero():
    # нетривиальный: отрицательные и ноль
    root = _build_bst([0, -2, 3, -5, -1, 2, 4])
    assert inorder(root) == [-5, -2, -1, 0, 2, 3, 4]
    assert preorder(root) == [0, -2, -5, -1, 3, 2, 4]
