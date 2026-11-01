from avl import AVL


def test_empty_search():
    # граница: пустое дерево
    tree = AVL()
    assert tree.search(1) is False
    assert tree.inorder() == []
    assert tree.is_balanced() is True


def test_single_insert_search_delete():
    # граница: один узел
    tree = AVL()
    tree.insert(10)
    assert tree.search(10) is True
    assert tree.search(11) is False
    assert tree.inorder() == [10]
    tree.delete(10)
    assert tree.root is None
    assert tree.search(10) is False


def test_insert_sorted_stays_balanced():
    # нетривиальный: возрастающая последовательность без AVL дала бы цепочку
    tree = AVL()
    for x in range(1, 8):
        tree.insert(x)
        assert tree.is_balanced()
    assert tree.inorder() == list(range(1, 8))
    assert tree.root is not None
    assert tree.root.key == 4


def test_insert_descending_rr_rotations():
    # типичный: убывающая последовательность, правые повороты / RR
    tree = AVL()
    for x in (3, 2, 1):
        tree.insert(x)
    assert tree.is_balanced()
    assert tree.root is not None and tree.root.key == 2
    assert tree.inorder() == [1, 2, 3]


def test_left_right_rotation():
    # вставка 3, 1, 2, LR вокруг 3
    tree = AVL()
    for x in (3, 1, 2):
        tree.insert(x)
    assert tree.root is not None and tree.root.key == 2
    assert tree.inorder() == [1, 2, 3]
    assert tree.is_balanced()


def test_right_left_rotation():
    # типичный: случай RL
    tree = AVL()
    for x in (1, 3, 2):
        tree.insert(x)
    assert tree.root is not None and tree.root.key == 2
    assert tree.inorder() == [1, 2, 3]
    assert tree.is_balanced()


def test_duplicate_ignored():
    # граница: повторная вставка того же ключа
    tree = AVL()
    tree.insert(5)
    tree.insert(5)
    assert tree.inorder() == [5]
    assert tree.root is not None
    assert tree.root.left is None and tree.root.right is None


def test_delete_leaf():
    # граница: удаление листа
    tree = AVL()
    for x in (2, 1, 3):
        tree.insert(x)
    tree.delete(1)
    assert tree.search(1) is False
    assert tree.inorder() == [2, 3]
    assert tree.is_balanced()


def test_delete_node_with_one_child():
    # типичный: узел с одним ребёнком
    tree = AVL()
    for x in (2, 1, 3, 4):
        tree.insert(x)
    tree.delete(3)
    assert tree.inorder() == [1, 2, 4]
    assert tree.is_balanced()


def test_delete_node_with_two_children():
    # типичный: замена на inorder-преемника
    tree = AVL()
    for x in (4, 2, 6, 1, 3, 5, 7):
        tree.insert(x)
    tree.delete(4)
    assert tree.search(4) is False
    assert tree.inorder() == [1, 2, 3, 5, 6, 7]
    assert tree.is_balanced()


def test_delete_missing_noop():
    # граница: удаление отсутствующего ключа
    tree = AVL()
    for x in (1, 2, 3):
        tree.insert(x)
    before = tree.inorder()
    tree.delete(99)
    assert tree.inorder() == before
    assert tree.is_balanced()


def test_delete_triggers_rebalance():
    # нетривиальный: удаление ломает баланс, поворот
    tree = AVL()
    for x in (1, 2, 3, 4, 5, 6, 7):
        tree.insert(x)
    tree.delete(1)
    tree.delete(2)
    tree.delete(3)
    assert tree.is_balanced()
    assert tree.inorder() == [4, 5, 6, 7]


def test_search_contains():
    # типичный: поиск существующих и нет
    tree = AVL()
    for x in (10, 5, 15, 3, 7, 12, 20):
        tree.insert(x)
    assert 7 in tree
    assert 11 not in tree
    assert tree.search(20) is True
    assert tree.search(1) is False


def test_mixed_insert_delete_sequence():
    # нетривиальный: смешанная последовательность операций
    tree = AVL()
    ops_insert = [50, 30, 70, 20, 40, 60, 80, 15, 25, 35]
    for x in ops_insert:
        tree.insert(x)
        assert tree.is_balanced()

    for x in (30, 70, 15, 50):
        tree.delete(x)
        assert tree.is_balanced()
        assert tree.search(x) is False

    remaining = sorted(set(ops_insert) - {30, 70, 15, 50})
    assert tree.inorder() == remaining
