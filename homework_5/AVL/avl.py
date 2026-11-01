from __future__ import annotations


class AVLNode:
    def __init__(self, key: int):
        self.key = key
        self.left: AVLNode | None = None
        self.right: AVLNode | None = None
        self.height = 1


class AVL:

    def __init__(self) -> None:
        self.root: AVLNode | None = None

    def insert(self, key: int) -> None:
        self.root = self._insert(self.root, key)

    def delete(self, key: int) -> None:
        self.root = self._delete(self.root, key)

    def search(self, key: int) -> bool:
        node = self.root
        while node is not None:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def __contains__(self, key: int) -> bool:
        return self.search(key)

    def inorder(self) -> list[int]:
        result: list[int] = []

        def dfs(node: AVLNode | None) -> None:
            if node is None:
                return
            dfs(node.left)
            result.append(node.key)
            dfs(node.right)

        dfs(self.root)
        return result

    def is_balanced(self) -> bool:

        def check(node: AVLNode | None) -> int:
            if node is None:
                return 0
            lh = check(node.left)
            if lh == -1:
                return -1
            rh = check(node.right)
            if rh == -1:
                return -1
            if abs(lh - rh) > 1:
                return -1
            h = 1 + max(lh, rh)
            if node.height != h:
                return -1
            return h

        return check(self.root) != -1

    @staticmethod
    def _height(node: AVLNode | None) -> int:
        return node.height if node is not None else 0

    def _update(self, node: AVLNode) -> None:
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node: AVLNode | None) -> int:
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, y: AVLNode) -> AVLNode:
        x = y.left
        assert x is not None
        t2 = x.right
        x.right = y
        y.left = t2
        self._update(y)
        self._update(x)
        return x

    def _rotate_left(self, x: AVLNode) -> AVLNode:
        y = x.right
        assert y is not None
        t2 = y.left
        y.left = x
        x.right = t2
        self._update(x)
        self._update(y)
        return y

    def _rebalance(self, node: AVLNode) -> AVLNode:
        self._update(node)
        bf = self._balance_factor(node)

        # Left Left
        if bf > 1 and self._balance_factor(node.left) >= 0:
            return self._rotate_right(node)
        # Left Right
        if bf > 1 and self._balance_factor(node.left) < 0:
            assert node.left is not None
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        # Right Right
        if bf < -1 and self._balance_factor(node.right) <= 0:
            return self._rotate_left(node)
        # Right Left
        if bf < -1 and self._balance_factor(node.right) > 0:
            assert node.right is not None
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _insert(self, node: AVLNode | None, key: int) -> AVLNode:
        if node is None:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node
        return self._rebalance(node)

    def _min_node(self, node: AVLNode) -> AVLNode:
        while node.left is not None:
            node = node.left
        return node

    def _delete(self, node: AVLNode | None, key: int) -> AVLNode | None:
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            succ = self._min_node(node.right)
            node.key = succ.key
            node.right = self._delete(node.right, succ.key)

        return self._rebalance(node)
