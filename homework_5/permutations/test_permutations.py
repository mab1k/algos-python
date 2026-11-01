import io
from itertools import permutations as py_permutations

from permutations import permute


def _sorted_perms(perms: list[list[int]]) -> list[list[int]]:
    return sorted(perms)


def test_example_123():
    # типичный: пример из условия
    assert _sorted_perms(permute([1, 2, 3])) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]


def test_example_01():
    # типичный: пример из условия
    assert _sorted_perms(permute([0, 1])) == [[0, 1], [1, 0]]


def test_example_single():
    # граница: один элемент
    assert permute([1]) == [[1]]


def test_empty():
    # граница: пустой массив, одна пустая перестановка
    assert permute([]) == [[]]


def test_matches_itertools():
    # нетривиальный: сверка с эталоном для n=4
    nums = [4, 1, 3, 2]
    expected = [list(p) for p in py_permutations(nums)]
    assert _sorted_perms(permute(nums)) == _sorted_perms(expected)


def test_count_is_factorial():
    # типичный: число перестановок = n!
    assert len(permute([1, 2, 3, 4])) == 24


def test_trace_shows_call_stack():
    # нетривиальный: визуализация стека через декоратор tracer
    buf = io.StringIO()
    result = permute([1, 2], trace=True, file=buf)
    assert _sorted_perms(result) == [[1, 2], [2, 1]]

    text = buf.getvalue()
    # корневой вход
    assert "-> step()" in text
    # вложенный вызов с отступом
    assert "  -> step()" in text
    # возвраты
    assert "<- step = None" in text
    assert "  <- step = None" in text


def test_with_duplicates_values_still_indexed():
    # граница: алгоритм идёт по индексам, при дубликатах значений
    # перестановки по позициям сохраняются
    result = permute([1, 1])
    assert len(result) == 2
    assert result[0] == [1, 1]
    assert result[1] == [1, 1]
