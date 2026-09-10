from prime import count_primes


def test_zero_and_one():
    # граница: N ≤ 1 — простых меньше N нет
    assert count_primes(0) == 0
    assert count_primes(1) == 0


def test_two():
    # граница: N = 2 — простых строго меньше 2 нет
    assert count_primes(2) == 0


def test_three():
    # граница: первое N, где появляется простое (только 2)
    assert count_primes(3) == 1


def test_example_ten():
    # типичный: пример из условия -> 2, 3, 5, 7
    assert count_primes(10) == 4


def test_prime_n_not_counted():
    # граница: само N простое, но нужно строго < N
    assert count_primes(11) == 4


def test_composite_after_prime():
    # типичный: N составное сразу после простого
    assert count_primes(12) == 5


def test_perfect_square_bound():
    # нетривиальный: N = 16 = 4² — граница внешнего цикла √N
    assert count_primes(16) == 6


def test_larger_range():
    # нетривиальный: больший диапазон, несколько проходов решета
    assert count_primes(30) == 10
    assert count_primes(100) == 25
