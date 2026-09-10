from sum import max_even_sum


def test_single_odd():
    # граница: один нечётный элемент — чётной суммы нет → 0
    assert max_even_sum([3]) == 0


def test_single_even():
    # граница: один чётный элемент — он и есть ответ
    assert max_even_sum([8]) == 8


def test_all_even():
    # граница: все чётные — берём полную сумму
    assert max_even_sum([2, 4, 8, 10]) == 24


def test_two_odds_even_sum():
    # граница: ровно два нечётных — сумма чётна, ничего не вычитаем
    assert max_even_sum([9, 11]) == 20


def test_three_odds_remove_one():
    # граница: нечётное число нечётных → убираем наименьшее
    assert max_even_sum([3, 3, 5]) == 8


def test_duplicates_even_total():
    # типичный/дубликаты: сумма уже чётная
    assert max_even_sum([3, 3, 5, 5]) == 16


def test_example_mixed():
    # типичный: смесь чётных и нечётных (пример из условия)
    assert max_even_sum([5, 7, 13, 2, 14]) == 36


def test_remove_smallest_odd_not_largest():
    # нетривиальный: при нечётной сумме вычитаем именно min нечётное
    assert max_even_sum([5, 11, 13, 2]) == 26


def test_many_odds_keep_maximum_even():
    # нетривиальный: много нечётных)
    assert max_even_sum([1, 3, 5, 7, 9, 2]) == 26
