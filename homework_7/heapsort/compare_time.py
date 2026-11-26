from __future__ import annotations

import random
import time

from heapsort import heapsort
from mergesort_ref import mergesort


def _bench(label: str, fn, data: list[int], mutate: bool) -> float:
    samples = []
    for _ in range(3):
        a = data[:]
        t0 = time.perf_counter()
        out = fn(a)
        dt = time.perf_counter() - t0
        samples.append(dt)
        expected = sorted(data)
        got = a if mutate else out
        assert got == expected, label
    return min(samples)


def main() -> None:
    rng = random.Random(0)
    sizes = [1_000, 5_000, 20_000, 50_000]
    rows: list[tuple[int, float, float, float]] = []

    for n in sizes:
        data = [rng.randrange(-10**9, 10**9) for _ in range(n)]
        t_heap = _bench("heapsort", heapsort, data, mutate=True)
        t_sorted = _bench("sorted", sorted, data, mutate=False)
        t_merge = _bench("mergesort", mergesort, data, mutate=False)
        rows.append((n, t_heap, t_sorted, t_merge))
        print(f"n={n:6d}  heapsort={t_heap:.4f}s  sorted={t_sorted:.4f}s  mergesort={t_merge:.4f}s")

    print("\n| n | heapsort | sorted() | mergesort |")
    print("|---|----------|----------|-----------|")
    for n, th, ts, tm in rows:
        print(f"| {n} | {th:.4f}s | {ts:.4f}s | {tm:.4f}s |")


if __name__ == "__main__":
    main()
