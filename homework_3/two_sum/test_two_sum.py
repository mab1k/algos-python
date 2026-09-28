from two_sum import two_sum


def test_example_first():
    # типичный: пример из условия [1, 3, 4, 10], k = 7 → 3 + 4
    assert two_sum([1, 3, 4, 10], 7) == (1, 2)


def test_example_duplicates():
    # типичный: дубликаты значений [5, 5, 1, 4], k = 10 → первые два 5
    assert two_sum([5, 5, 1, 4], 10) == (0, 1)


def test_pair_at_ends():
    # граница: пара — первый и последний элементы
    assert two_sum([2, 9, 1, 5], 7) == (0, 3)


def test_pair_adjacent_start():
    # граница: пара в начале массива
    assert two_sum([4, 6, 1, 2], 10) == (0, 1)


def test_pair_adjacent_end():
    # граница: пара в конце массива
    assert two_sum([1, 2, 3, 7], 10) == (2, 3)


def test_minimal_length():
    # граница: ровно два элемента
    assert two_sum([3, 4], 7) == (0, 1)


def test_negatives():
    # нетривиальный: отрицательные числа
    assert two_sum([-3, 1, 8, -5], 5) == (0, 2)


def test_zero_target():
    # нетривиальный: сумма равна нулю (положительное + отрицательное)
    assert two_sum([4, -2, 7, -4], 0) == (0, 3)


def test_same_value_not_same_index():
    # нетривиальный: нужны два разных индекса с одинаковым значением
    assert two_sum([1, 7, 7, 3], 14) == (1, 2)
