from __future__ import annotations


def mergesort_iterative(arr: list[int]) -> list[int]:
    n = len(arr)
    if n <= 1:
        return arr[:]

    a = arr[:]
    width = 1
    while width < n:
        buf: list[int] = []
        for left in range(0, n, 2 * width):
            mid = min(left + width, n)
            right = min(left + 2 * width, n)
            buf.extend(_merge(a[left:mid], a[mid:right]))
        a = buf
        width *= 2
    return a


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


def quicksort_iterative(arr: list[int]) -> list[int]:
    a = arr[:]
    if len(a) <= 1:
        return a

    stack: list[tuple[int, int]] = [(0, len(a) - 1)]
    while stack:
        lo, hi = stack.pop()
        if lo >= hi:
            continue
        p = _partition(a, lo, hi)
        left_size = p - 1 - lo
        right_size = hi - (p + 1)
        if left_size > right_size:
            stack.append((lo, p - 1))
            stack.append((p + 1, hi))
        else:
            stack.append((p + 1, hi))
            stack.append((lo, p - 1))
    return a


def _partition(a: list[int], lo: int, hi: int) -> int:
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    return i
