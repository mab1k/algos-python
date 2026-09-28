import pytest

from hash_table import HashTable


def test_empty_initially():
    # граница: новая таблица пуста
    ht = HashTable()
    assert len(ht) == 0
    assert ht.get("x") is None
    assert ("x" in ht) is False


def test_put_and_get():
    # типичный: вставка и поиск
    ht = HashTable()
    ht.put("a", 1)
    ht.put("b", 2)
    assert ht.get("a") == 1
    assert ht.get("b") == 2
    assert len(ht) == 2


def test_update_existing_key():
    # типичный: повторная вставка обновляет значение, размер не растёт
    ht = HashTable()
    ht.put("x", 10)
    ht.put("x", 20)
    assert ht.get("x") == 20
    assert len(ht) == 1


def test_delete_existing():
    # типичный: удаление существующего ключа
    ht = HashTable()
    ht.put("a", 1)
    ht.put("b", 2)
    assert ht.delete("a") is True
    assert ht.get("a") is None
    assert len(ht) == 1
    assert ht.get("b") == 2


def test_delete_missing():
    # граница: удаление отсутствующего ключа
    ht = HashTable()
    ht.put("a", 1)
    assert ht.delete("missing") is False
    assert len(ht) == 1


def test_get_default():
    # граница: get с default для отсутствующего ключа
    ht = HashTable()
    assert ht.get("no", -1) == -1


def test_contains_and_dunder():
    # типичный: операторы in / [] 
    ht = HashTable()
    ht["k"] = 42
    assert "k" in ht
    assert ht["k"] == 42
    del ht["k"]
    assert "k" not in ht


def test_getitem_missing_raises():
    # граница: [] для отсутствующего ключа → KeyError
    ht = HashTable()
    with pytest.raises(KeyError):
        _ = ht["no"]


def test_delitem_missing_raises():
    # граница: del отсутствующего ключа → KeyError
    ht = HashTable()
    with pytest.raises(KeyError):
        del ht["no"]


def test_various_key_types():
    # нетривиальный: разные хешируемые типы ключей
    ht = HashTable()
    ht.put(1, "int")
    ht.put("1", "str")
    ht.put((1, 2), "tuple")
    assert ht.get(1) == "int"
    assert ht.get("1") == "str"
    assert ht.get((1, 2)) == "tuple"
    assert len(ht) == 3


def test_collision_double_hashing():
    # нетривиальный: коллизии разрешаются двойным хешированием (малая ёмкость)
    ht = HashTable(capacity=1)
    ht.put("a", 1)
    ht.put("b", 2)
    ht.put("c", 3)
    assert ht.get("a") == 1
    assert ht.get("b") == 2
    assert ht.get("c") == 3
    assert len(ht) == 3


def test_delete_does_not_break_probe_chain():
    # нетривиальный: tombstone не обрывает поиск ключа дальше по пробе
    ht = HashTable(capacity=8)
    keys = list(range(6))
    for k in keys:
        ht.put(k, k * 10)
    mid = keys[2]
    assert ht.delete(mid) is True
    for k in keys:
        if k == mid:
            assert ht.get(k) is None
        else:
            assert ht.get(k) == k * 10


def test_resize_preserves_entries():
    # нетривиальный: после расширения все ключи доступны
    ht = HashTable(capacity=2)
    for i in range(20):
        ht.put(i, i * 10)
    assert len(ht) == 20
    for i in range(20):
        assert ht.get(i) == i * 10
    assert ht._capacity >= 32


def test_keys_values_items():
    # типичный: обход содержимого
    ht = HashTable()
    ht.put("a", 1)
    ht.put("b", 2)
    assert sorted(ht.keys()) == ["a", "b"]
    assert sorted(ht.values()) == [1, 2]
    assert sorted(ht.items()) == [["a", 1], ["b", 2]]


def test_delete_then_reinsert():
    # нетривиальный: удалили и снова вставили тот же ключ
    ht = HashTable()
    ht.put("x", 1)
    ht.delete("x")
    ht.put("x", 2)
    assert ht.get("x") == 2
    assert len(ht) == 1


def test_load_factor_triggers_resize():
    # граница: при load >= 0.75 ёмкость удваивается, данные сохраняются
    ht = HashTable(capacity=4)
    ht.put("a", 1)
    ht.put("b", 2)
    ht.put("c", 3)
    assert ht._capacity == 4
    assert ht.load_factor() == 0.75
    ht.put("d", 4)
    assert ht._capacity == 8
    assert len(ht) == 4
    assert ht.get("a") == 1 and ht.get("d") == 4
