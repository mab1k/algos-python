from __future__ import annotations

import random

import pytest

from kth import find_kth_largest, find_kth_largest_heapq


IMPLEMENTATIONS = (find_kth_largest, find_kth_largest_heapq)


@pytest.mark.parametrize("fn", IMPLEMENTATIONS)
def test_example_1(fn):
    assert fn([3, 2, 1, 5, 6, 4], 2) == 5


@pytest.mark.parametrize("fn", IMPLEMENTATIONS)
def test_example_2(fn):
    assert fn([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


@pytest.mark.parametrize("fn", IMPLEMENTATIONS)
def test_k_equals_1_is_max(fn):
    assert fn([7, 1, 9, 3], 1) == 9


@pytest.mark.parametrize("fn", IMPLEMENTATIONS)
def test_k_equals_n_is_min(fn):
    assert fn([7, 1, 9, 3], 4) == 1


@pytest.mark.parametrize("fn", IMPLEMENTATIONS)
def test_single(fn):
    assert fn([42], 1) == 42


@pytest.mark.parametrize("fn", IMPLEMENTATIONS)
def test_all_equal(fn):
    assert fn([2, 2, 2, 2], 3) == 2


@pytest.mark.parametrize("fn", IMPLEMENTATIONS)
def test_negatives(fn):
    assert fn([-1, -5, -2, -8], 2) == -2


@pytest.mark.parametrize("fn", IMPLEMENTATIONS)
def test_does_not_mutate(fn):
    nums = [3, 2, 1, 5, 6, 4]
    fn(nums, 2)
    assert nums == [3, 2, 1, 5, 6, 4]


@pytest.mark.parametrize("fn", IMPLEMENTATIONS)
def test_matches_sorted_random(fn):
    rng = random.Random(1)
    for _ in range(40):
        n = rng.randint(1, 80)
        nums = [rng.randrange(-100, 100) for _ in range(n)]
        k = rng.randint(1, n)
        expected = sorted(nums, reverse=True)[k - 1]
        assert fn(nums, k) == expected


@pytest.mark.parametrize("fn", IMPLEMENTATIONS)
def test_invalid_k(fn):
    with pytest.raises(ValueError):
        fn([1, 2, 3], 0)
    with pytest.raises(ValueError):
        fn([1, 2, 3], 4)
    with pytest.raises(ValueError):
        fn([], 1)


def test_both_implementations_agree():
    rng = random.Random(7)
    for _ in range(30):
        n = rng.randint(1, 50)
        nums = [rng.randrange(-50, 50) for _ in range(n)]
        k = rng.randint(1, n)
        assert find_kth_largest(nums, k) == find_kth_largest_heapq(nums, k)
