from __future__ import annotations


def _sift_down_max(arr: list[int], i: int, n: int) -> None:
    """Опускает arr[i] в max-heap на префиксе arr[0:n]."""
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest == i:
            break
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest


def _build_maxheap(arr: list[int]) -> None:
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        _sift_down_max(arr, i, n)


def heapsort(arr: list[int]) -> list[int]:
    n = len(arr)
    if n <= 1:
        return arr

    _build_maxheap(arr)
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        _sift_down_max(arr, 0, end)
    return arr
