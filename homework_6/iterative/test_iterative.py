from __future__ import annotations

import random

from iterative_sorts import mergesort_iterative, quicksort_iterative


def test_basic():
    assert mergesort_iterative([3, 1, 2]) == [1, 2, 3]
    assert quicksort_iterative([3, 1, 2]) == [1, 2, 3]


def test_empty_single():
    assert mergesort_iterative([]) == []
    assert quicksort_iterative([]) == []
    assert mergesort_iterative([5]) == [5]
    assert quicksort_iterative([5]) == [5]


def test_already_sorted_and_reversed():
    data = list(range(50))
    rev = list(reversed(data))
    assert mergesort_iterative(data) == data
    assert quicksort_iterative(data) == data
    assert mergesort_iterative(rev) == data
    assert quicksort_iterative(rev) == data


def test_duplicates_negatives():
    nums = [0, -2, 3, -2, 0, 1]
    assert mergesort_iterative(nums) == sorted(nums)
    assert quicksort_iterative(nums) == sorted(nums)


def test_does_not_mutate():
    nums = [9, 8, 7]
    mergesort_iterative(nums)
    quicksort_iterative(nums)
    assert nums == [9, 8, 7]


def test_matches_builtin_random():
    rng = random.Random(42)
    data = [rng.randrange(-1000, 1000) for _ in range(500)]
    expected = sorted(data)
    assert mergesort_iterative(data) == expected
    assert quicksort_iterative(data) == expected
