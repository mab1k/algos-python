from __future__ import annotations

import random
import sys

from recursive_sorts import mergesort, quicksort
from timed import timed


def test_mergesort_basic():
    assert mergesort([3, 1, 2]) == [1, 2, 3]


def test_quicksort_basic():
    assert quicksort([3, 1, 2]) == [1, 2, 3]


def test_empty_and_single():
    assert mergesort([]) == []
    assert quicksort([]) == []
    assert mergesort([7]) == [7]
    assert quicksort([7]) == [7]


def test_duplicates_and_negatives():
    nums = [2, -1, 2, 0, -1, 5]
    assert mergesort(nums) == sorted(nums)
    assert quicksort(nums) == sorted(nums)


def test_does_not_mutate_input():
    nums = [4, 3, 2, 1]
    mergesort(nums)
    quicksort(nums)
    assert nums == [4, 3, 2, 1]


def test_timed_records_time():
    @timed
    def work(n: int) -> int:
        s = 0
        for i in range(n):
            s += i
        return s

    assert work(10_000) == sum(range(10_000))
    assert work.last_time > 0


def test_sorted_input_quicksort_slower_than_mergesort():
    # Глубина рекурсии ≈ n
    n = 3500
    data = list(range(n))
    old_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(n + 100)

    @timed
    def run_merge(a: list[int]) -> list[int]:
        return mergesort(a)

    @timed
    def run_quick(a: list[int]) -> list[int]:
        return quicksort(a)

    try:
        assert run_merge(data) == data
        assert run_quick(data) == data
    finally:
        sys.setrecursionlimit(old_limit)

    # quicksort должен быть заметно медленнее mergesort
    assert run_quick.last_time > 3 * run_merge.last_time


def test_random_similar_order():
    # На случайных данных оба около O(n log n), оба корректны.
    rng = random.Random(0)
    data = [rng.randrange(-10_000, 10_000) for _ in range(2000)]
    expected = sorted(data)
    assert mergesort(data) == expected
    assert quicksort(data) == expected
