from palindrome import is_palindrome


def test_zero():
    # граница: 0 — одноразрядное и одновременно оканчивается на 0
    assert is_palindrome(0) is True


def test_single_digits():
    # граница: все числа 1..9 — палиндромы без разворота
    for d in range(1, 10):
        assert is_palindrome(d) is True


def test_negative():
    # граница: отрицательные не считаем палиндромами по условию задачи
    assert is_palindrome(-1) is False
    assert is_palindrome(-121) is False


def test_trailing_zero():
    # граница: положительное с нулём в конце не может быть палиндромом
    assert is_palindrome(10) is False
    assert is_palindrome(100) is False
    assert is_palindrome(123210) is False


def test_typical_odd_length_palindrome():
    # типичный: нечётная длина, разворот совпадает
    assert is_palindrome(12321) is True


def test_typical_even_length_palindrome():
    # типичный: чётная длина
    assert is_palindrome(1221) is True


def test_near_miss_not_palindrome():
    # типичный: почти палиндром, но не совпадает
    assert is_palindrome(123421) is False


def test_zeros_in_the_middle():
    # нетривиальный: нули внутри числа не должны исчезать при развороте
    assert is_palindrome(1000001) is True
    assert is_palindrome(1001001) is True
    assert is_palindrome(101001) is False


def test_large_integer():
    # нетривиальный: длинное число без ограничения разрядности int
    n = 9876543210123456789
    assert is_palindrome(n) is True
    assert is_palindrome(n + 1) is False
