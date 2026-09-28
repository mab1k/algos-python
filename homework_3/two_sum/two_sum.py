def two_sum(arr: list[int], k: int) -> tuple[int, int]:
    seen: dict[int, int] = {}

    for i, value in enumerate(arr):
        need = k - value
        if need in seen:
            left, right = seen[need], i
            return (left, right) if left < right else (right, left)
        seen[value] = i

    raise ValueError("pair not found")
