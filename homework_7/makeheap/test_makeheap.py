from __future__ import annotations

import random
import time

from makeheap import is_minheap, makeheap, makeheap_n_log_n


def test_empty_and_single():
    assert makeheap([]) == []
    assert makeheap_n_log_n([]) == []
    assert is_minheap([])
    assert makeheap([7]) == [7]
    assert makeheap_n_log_n([7]) == [7]
    assert is_minheap([7])


def test_examples_become_minheap():
    for builder in (makeheap, makeheap_n_log_n):
        a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        builder(a)
        assert is_minheap(a)
        assert sorted(a) == [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]


def test_already_heap():
    a = [1, 2, 3, 4, 5]
    assert is_minheap(a)
    makeheap(a)
    assert is_minheap(a)
    b = [1, 2, 3, 4, 5]
    makeheap_n_log_n(b)
    assert is_minheap(b)


def test_reversed():
    a = [5, 4, 3, 2, 1]
    makeheap(a)
    assert is_minheap(a)
    assert a[0] == 1


def test_duplicates():
    a = [3, 1, 3, 1, 2, 2]
    makeheap(a)
    assert is_minheap(a)
    makeheap_n_log_n([3, 1, 3, 1, 2, 2])
    b = [3, 1, 3, 1, 2, 2]
    makeheap_n_log_n(b)
    assert is_minheap(b)


def test_negatives():
    a = [-1, -5, 0, -2, 4]
    makeheap(a)
    assert is_minheap(a)
    assert a[0] == -5


def test_random_both_builders():
    rng = random.Random(42)
    for _ in range(40):
        n = rng.randint(0, 100)
        data = [rng.randrange(-500, 500) for _ in range(n)]
        a = data[:]
        b = data[:]
        makeheap(a)
        makeheap_n_log_n(b)
        assert is_minheap(a)
        assert is_minheap(b)
        assert sorted(a) == sorted(data)
        assert sorted(b) == sorted(data)


def test_inplace_returns_same_object():
    a = [9, 3, 7, 1]
    assert makeheap(a) is a
    b = [9, 3, 7, 1]
    assert makeheap_n_log_n(b) is b


def _time_builder(builder, data: list[int], repeats: int = 3) -> float:
    best = float("inf")
    for _ in range(repeats):
        a = data[:]
        t0 = time.perf_counter()
        builder(a)
        best = min(best, time.perf_counter() - t0)
        assert is_minheap(a)
    return best


def test_compare_times_linear_faster_on_large_n():
    n = 300_000
    data = list(range(n, 0, -1))

    t_linear = _time_builder(makeheap, data)
    t_nlogn = _time_builder(makeheap_n_log_n, data)

    print(f"\nвход: убывающий, n={n}")
    print(f"makeheap O(N):        {t_linear:.4f}s")
    print(f"makeheap_n_log_n:     {t_nlogn:.4f}s")
    print(f"отношение nlogn/N:    {t_nlogn / t_linear:.2f}x")

    assert t_linear < t_nlogn
    assert t_nlogn > 1.5 * t_linear
