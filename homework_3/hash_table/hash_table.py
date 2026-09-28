class HashTable:

    _EMPTY = None
    _DELETED = object()
    _MISSING = object()

    _DEFAULT_CAPACITY = 8
    _LOAD_FACTOR = 0.75

    def __init__(self, capacity: int = _DEFAULT_CAPACITY):
        if capacity < 1:
            raise ValueError("capacity must be positive")
        self._capacity = self._next_power_of_2(capacity)
        self._size = 0
        self._tombstones = 0
        # слот: None | _DELETED | [key, value]
        self._slots: list = [self._EMPTY] * self._capacity

    @staticmethod
    def _next_power_of_2(n: int) -> int:
        p = 1
        while p < n:
            p *= 2
        return p

    def __len__(self) -> int:
        return self._size

    def __contains__(self, key) -> bool:
        return self.get(key, self._MISSING) is not self._MISSING

    def __setitem__(self, key, value) -> None:
        self.put(key, value)

    def __getitem__(self, key):
        value = self.get(key, self._MISSING)
        if value is self._MISSING:
            raise KeyError(key)
        return value

    def __delitem__(self, key) -> None:
        if not self.delete(key):
            raise KeyError(key)

    def load_factor(self) -> float:
        return self._size / self._capacity

    def _h1(self, key) -> int:
        return abs(hash(key)) % self._capacity

    def _h2(self, key) -> int:
        """Шаг зондирования: нечётный → взаимно прост с ёмкостью 2^k."""
        if self._capacity == 1:
            return 1
        return (abs(hash(key)) % (self._capacity // 2)) * 2 + 1

    def _probe(self, key):
        """Индексы: (h1(key) + i * h2(key)) % capacity, i = 0, 1, …"""
        start = self._h1(key)
        step = self._h2(key)
        for i in range(self._capacity):
            yield (start + i * step) % self._capacity

    def _occupied_ratio(self) -> float:
        return (self._size + self._tombstones) / self._capacity

    def _resize(self, new_capacity: int) -> None:
        old_slots = self._slots
        self._capacity = new_capacity
        self._slots = [self._EMPTY] * new_capacity
        self._size = 0
        self._tombstones = 0
        for slot in old_slots:
            if slot is not self._EMPTY and slot is not self._DELETED:
                self.put(slot[0], slot[1])

    def put(self, key, value) -> None:
        """Вставка или обновление значения по ключу."""
        if self._occupied_ratio() >= self._LOAD_FACTOR:
            self._resize(self._capacity * 2)

        first_deleted = None
        for idx in self._probe(key):
            slot = self._slots[idx]
            if slot is self._EMPTY:
                place = first_deleted if first_deleted is not None else idx
                if place == first_deleted:
                    self._tombstones -= 1
                self._slots[place] = [key, value]
                self._size += 1
                return
            if slot is self._DELETED:
                if first_deleted is None:
                    first_deleted = idx
                continue
            if slot[0] == key:
                slot[1] = value
                return

        self._resize(self._capacity * 2)
        self.put(key, value)

    def get(self, key, default=None):
        """Поиск значения по ключу; если нет — default."""
        for idx in self._probe(key):
            slot = self._slots[idx]
            if slot is self._EMPTY:
                return default
            if slot is self._DELETED:
                continue
            if slot[0] == key:
                return slot[1]
        return default

    def delete(self, key) -> bool:
        """Удаление по ключу. True, если ключ был; False иначе."""
        for idx in self._probe(key):
            slot = self._slots[idx]
            if slot is self._EMPTY:
                return False
            if slot is self._DELETED:
                continue
            if slot[0] == key:
                self._slots[idx] = self._DELETED
                self._size -= 1
                self._tombstones += 1
                return True
        return False

    def keys(self) -> list:
        result: list = []
        for slot in self._slots:
            if slot is not self._EMPTY and slot is not self._DELETED:
                result.append(slot[0])
        return result

    def values(self) -> list:
        result: list = []
        for slot in self._slots:
            if slot is not self._EMPTY and slot is not self._DELETED:
                result.append(slot[1])
        return result

    def items(self) -> list:
        result: list = []
        for slot in self._slots:
            if slot is not self._EMPTY and slot is not self._DELETED:
                result.append([slot[0], slot[1]])
        return result
