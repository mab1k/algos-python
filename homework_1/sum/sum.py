def max_even_sum(nums: list[int]) -> int:
    total = sum(nums)
    if total % 2 == 0:
        return total

    smallest_odd = min(n for n in nums if n % 2 == 1)
    return total - smallest_odd
