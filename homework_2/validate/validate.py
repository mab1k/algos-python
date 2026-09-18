def validate(pushed: list[int], popped: list[int]) -> bool:
    stack: list[int] = []
    j = 0
    n = len(popped)

    for x in pushed:
        stack.append(x)
        while stack and j < n and stack[-1] == popped[j]:
            stack.pop()
            j += 1

    return j == n
