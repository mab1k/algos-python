from __future__ import annotations


def find_kth_largest(nums: list[int], k: int) -> int:
    if not nums:
        raise ValueError("nums is empty")
    if k < 1 or k > len(nums):
        raise ValueError("k out of range")

    a = nums[:]
    target = len(a) - k
    lo, hi = 0, len(a) - 1
    while True:
        p = _partition(a, lo, hi)
        if p == target:
            return a[p]
        if p < target:
            lo = p + 1
        else:
            hi = p - 1


def _partition(a: list[int], lo: int, hi: int) -> int:
    mid = (lo + hi) // 2
    if a[mid] < a[lo]:
        a[lo], a[mid] = a[mid], a[lo]
    if a[hi] < a[lo]:
        a[lo], a[hi] = a[hi], a[lo]
    if a[mid] < a[hi]:
        a[mid], a[hi] = a[hi], a[mid]

    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    return i
