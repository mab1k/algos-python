from __future__ import annotations

import random

import pytest

from kth import find_kth_largest


def test_example_1():
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5


def test_example_2():
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


def test_k_equals_1_is_max():
    assert find_kth_largest([7, 1, 9, 3], 1) == 9


def test_k_equals_n_is_min():
    assert find_kth_largest([7, 1, 9, 3], 4) == 1


def test_single():
    assert find_kth_largest([42], 1) == 42


def test_all_equal():
    assert find_kth_largest([2, 2, 2, 2], 3) == 2


def test_negatives():
    assert find_kth_largest([-1, -5, -2, -8], 2) == -2


def test_does_not_mutate():
    nums = [3, 2, 1, 5, 6, 4]
    find_kth_largest(nums, 2)
    assert nums == [3, 2, 1, 5, 6, 4]


def test_matches_sorted_random():
    rng = random.Random(1)
    for _ in range(30):
        n = rng.randint(1, 80)
        nums = [rng.randrange(-100, 100) for _ in range(n)]
        k = rng.randint(1, n)
        expected = sorted(nums, reverse=True)[k - 1]
        assert find_kth_largest(nums, k) == expected


def test_invalid_k():
    with pytest.raises(ValueError):
        find_kth_largest([1, 2, 3], 0)
    with pytest.raises(ValueError):
        find_kth_largest([1, 2, 3], 4)
