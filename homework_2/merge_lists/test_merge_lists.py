from merge_lists import ListNode, merge_with_dummy, merge_without_dummy


def to_list(head: ListNode | None) -> list[int]:
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next
    return result


def from_list(values: list[int]) -> ListNode | None:
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def _check_both(a: list[int], b: list[int], expected: list[int]) -> None:
    assert to_list(merge_with_dummy(from_list(a), from_list(b))) == expected
    assert to_list(merge_without_dummy(from_list(a), from_list(b))) == expected


def test_example_from_statement():
    # типичный: пример из условия
    _check_both([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])


def test_both_empty():
    # граница: оба списка пусты
    _check_both([], [], [])


def test_one_empty():
    # граница: один из списков пуст
    _check_both([], [1, 2, 3], [1, 2, 3])
    _check_both([1, 2, 3], [], [1, 2, 3])


def test_single_nodes():
    # граница: по одному узлу
    _check_both([1], [2], [1, 2])
    _check_both([1], [1], [1, 1])


def test_no_overlap_order():
    # типичный: все элементы одного списка меньше другого
    _check_both([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6])


def test_duplicates_across_lists():
    # типичный: одинаковые значения в обоих списках
    _check_both([1, 1, 2], [1, 2, 2], [1, 1, 1, 2, 2, 2])


def test_different_lengths():
    # нетривиальный: сильно разная длина
    _check_both([1], [2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6])
    _check_both([1, 3, 5, 7, 9], [2], [1, 2, 3, 5, 7, 9])


def test_interleaved_values():
    # нетривиальный: значения чередуются
    _check_both([1, 3, 5, 7], [2, 4, 6, 8], [1, 2, 3, 4, 5, 6, 7, 8])


def test_negative_and_zero():
    # нетривиальный: отрицательные и ноль
    _check_both([-5, -1, 0], [-3, 2], [-5, -3, -1, 0, 2])
