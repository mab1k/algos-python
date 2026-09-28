def _signature(word: str) -> tuple[int, ...]:
    counts = [0] * 26
    for ch in word:
        counts[ord(ch) - ord("a")] += 1
    return tuple(counts)


def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups: dict[tuple[int, ...], list[str]] = {}

    for word in strs:
        key = _signature(word)
        if key not in groups:
            groups[key] = []
        groups[key].append(word)

    return list(groups.values())
