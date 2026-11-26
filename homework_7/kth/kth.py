from __future__ import annotations

import heapq


def _sift_up(heap: list[int], i: int) -> None:
    while i > 0:
        parent = (i - 1) // 2
        if heap[i] >= heap[parent]:
            break
        heap[i], heap[parent] = heap[parent], heap[i]
        i = parent


def _sift_down(heap: list[int], i: int) -> None:
    n = len(heap)
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < n and heap[left] < heap[smallest]:
            smallest = left
        if right < n and heap[right] < heap[smallest]:
            smallest = right
        if smallest == i:
            break
        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest


def _heap_push(heap: list[int], value: int) -> None:
    heap.append(value)
    _sift_up(heap, len(heap) - 1)


def _heap_replace_root(heap: list[int], value: int) -> None:
    heap[0] = value
    _sift_down(heap, 0)


def find_kth_largest(nums: list[int], k: int) -> int:
    if not nums:
        raise ValueError("nums is empty")
    if k < 1 or k > len(nums):
        raise ValueError("k out of range")

    heap: list[int] = []
    for x in nums:
        if len(heap) < k:
            _heap_push(heap, x)
        elif x > heap[0]:
            _heap_replace_root(heap, x)
    return heap[0]


def find_kth_largest_heapq(nums: list[int], k: int) -> int:
    if not nums:
        raise ValueError("nums is empty")
    if k < 1 or k > len(nums):
        raise ValueError("k out of range")

    heap: list[int] = []
    for x in nums:
        if len(heap) < k:
            heapq.heappush(heap, x)
        elif x > heap[0]:
            heapq.heapreplace(heap, x)
    return heap[0]
