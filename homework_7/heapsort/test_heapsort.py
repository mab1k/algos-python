from __future__ import annotations

import random

from heapsort import heapsort
from mergesort_ref import mergesort


def test_empty_and_single():
    assert heapsort([]) == []
    assert heapsort([7]) == [7]


def test_basic():
    a = [4, 1, 3, 2]
    assert heapsort(a) == [1, 2, 3, 4]
    assert a == [1, 2, 3, 4]


def test_already_sorted():
    a = [1, 2, 3, 4, 5]
    heapsort(a)
    assert a == [1, 2, 3, 4, 5]


def test_reversed():
    a = [5, 4, 3, 2, 1]
    heapsort(a)
    assert a == [1, 2, 3, 4, 5]


def test_duplicates_and_negatives():
    a = [2, -1, 2, 0, -1, 5]
    expected = sorted(a)
    heapsort(a)
    assert a == expected


def test_inplace_same_object():
    a = [3, 1, 2]
    assert heapsort(a) is a


def test_random_matches_sorted():
    rng = random.Random(3)
    for _ in range(30):
        n = rng.randint(0, 80)
        data = [rng.randrange(-200, 200) for _ in range(n)]
        a = data[:]
        heapsort(a)
        assert a == sorted(data)


def test_agrees_with_mergesort():
    rng = random.Random(11)
    data = [rng.randrange(-1000, 1000) for _ in range(500)]
    a = data[:]
    heapsort(a)
    assert a == mergesort(data)
