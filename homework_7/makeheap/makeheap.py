from __future__ import annotations


def _sift_up(arr: list[int], i: int) -> None:
    while i > 0:
        parent = (i - 1) // 2
        if arr[i] >= arr[parent]:
            break
        arr[i], arr[parent] = arr[parent], arr[i]
        i = parent


def _sift_down(arr: list[int], i: int, n: int) -> None:
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right
        if smallest == i:
            break
        arr[i], arr[smallest] = arr[smallest], arr[i]
        i = smallest


def makeheap_n_log_n(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        _sift_up(arr, i)
    return arr


def makeheap(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        _sift_down(arr, i, n)
    return arr


def is_minheap(arr: list[int]) -> bool:
    n = len(arr)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
    return True
