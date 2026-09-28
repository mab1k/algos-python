from anagrams import group_anagrams


def _normalize(groups: list[list[str]]) -> list[list[str]]:
    return sorted((sorted(g) for g in groups), key=lambda g: (g, len(g)))


def test_example_from_statement():
    # типичный: пример из условия
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert _normalize(result) == _normalize(expected)


def test_empty_list():
    # граница: пустой вход
    assert group_anagrams([]) == []


def test_single_word():
    # граница: одно слово — одна группа из него
    assert group_anagrams(["hello"]) == [["hello"]]


def test_all_identical():
    # граница: все слова одинаковые — одна группа
    assert _normalize(group_anagrams(["aa", "aa", "aa"])) == [["aa", "aa", "aa"]]


def test_no_anagrams():
    # граница: ни одна пара не является анаграммами
    result = group_anagrams(["abc", "def", "ghi"])
    assert _normalize(result) == [["abc"], ["def"], ["ghi"]]


def test_empty_strings():
    # граница: пустые строки — анаграммы друг друга
    result = group_anagrams(["", "", "a"])
    assert _normalize(result) == [["", ""], ["a"]]


def test_same_letters_different_counts():
    # нетривиальный: общие буквы, но разный мультисет → разные группы
    result = group_anagrams(["aab", "abb", "abab", "baba"])
    expected = [["aab"], ["abb"], ["abab", "baba"]]
    assert _normalize(result) == _normalize(expected)


def test_single_char_words():
    # граница: однобуквенные слова
    result = group_anagrams(["a", "b", "a", "c", "b"])
    expected = [["a", "a"], ["b", "b"], ["c"]]
    assert _normalize(result) == _normalize(expected)


def test_long_anagram_chain():
    # нетривиальный: длинные слова и несколько независимых групп
    result = group_anagrams(
        ["listen", "silent", "enlist", "google", "googel", "xyz", "zyx"]
    )
    expected = [
        ["enlist", "listen", "silent"],
        ["googel", "google"],
        ["xyz", "zyx"],
    ]
    assert _normalize(result) == _normalize(expected)
