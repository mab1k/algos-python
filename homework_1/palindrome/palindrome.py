def is_palindrome(num: int) -> bool:
    if num < 0:
        return False
    if num < 10:
        return True
    if num % 10 == 0:
        return False
    original = num
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num = num // 10
    return reversed_num == original

