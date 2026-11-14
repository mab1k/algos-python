from __future__ import annotations


def mergesort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return _merge(left, right)


def _merge(left: list[int], right: list[int]) -> list[int]:
    result: list[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quicksort(arr: list[int]) -> list[int]:
    a = arr[:]
    _quicksort(a, 0, len(a) - 1)
    return a


def _quicksort(a: list[int], lo: int, hi: int) -> None:
    if lo >= hi:
        return
    p = _partition(a, lo, hi)
    _quicksort(a, lo, p - 1)
    _quicksort(a, p + 1, hi)


def _partition(a: list[int], lo: int, hi: int) -> int:
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    return i
