from __future__ import annotations

import sys
from pathlib import Path
from typing import TextIO

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tracer"))
from tracer import tracer  # noqa: E402


def permute(
    nums: list[int],
    *,
    trace: bool = False,
    file: TextIO | None = None,
) -> list[list[int]]:

    result: list[list[int]] = []
    n = len(nums)
    used = [False] * n
    path: list[int] = []

    def step() -> None:
        if len(path) == n:
            result.append(path.copy())
            return
        for i in range(n):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            step()
            path.pop()
            used[i] = False

    if trace:
        step = tracer(file=file)(step)

    step()
    return result
