from validate import validate


def test_example_true():
    # типичный: пример 1 из условия
    assert validate([1, 2, 3, 4, 5], [1, 3, 5, 4, 2]) is True


def test_example_false():
    # типичный: пример 2 из условия
    assert validate([1, 2, 3], [3, 1, 2]) is False


def test_single_element():
    # граница: один элемент
    assert validate([1], [1]) is True


def test_push_all_then_pop_all():
    # граница: сначала все push, потом pop в обратном порядке
    assert validate([1, 2, 3, 4], [4, 3, 2, 1]) is True


def test_immediate_pop_each():
    # граница: после каждого push сразу pop — popped == pushed
    assert validate([1, 2, 3, 4], [1, 2, 3, 4]) is True


def test_impossible_pop_order():
    # типичный: нельзя вытащить меньший раньше большего при такой pushed
    assert validate([1, 2, 3, 4], [4, 1, 2, 3]) is False


def test_two_elements_both_orders():
    # граница: два элемента, оба допустимых порядка
    assert validate([1, 2], [1, 2]) is True
    assert validate([1, 2], [2, 1]) is True


def test_large_sequence_pattern():
    # нетривиальный: длинная последовательность
    n = 1000
    pushed = list(range(n))
    popped = []
    i = 0
    while i + 1 < n:
        popped.extend([i + 1, i])
        i += 2
    if i < n:
        popped.append(i)
    assert validate(pushed, popped) is True
