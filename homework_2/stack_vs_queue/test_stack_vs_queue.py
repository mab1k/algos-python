import pytest

from stack_vs_queue import Queue, Stack


# --- Stack ---


def test_stack_empty_initially():
    # граница: новый стек пуст
    s = Stack()
    assert s.is_empty() is True
    assert s.size() == 0


def test_stack_push_peek_pop_lifo():
    # типичный: последний добавленный выходит первым
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.peek() == 3
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty() is True


def test_stack_size_after_operations():
    # типичный: size отражает число элементов
    s = Stack()
    s.push(10)
    s.push(20)
    assert s.size() == 2
    s.pop()
    assert s.size() == 1


def test_stack_pop_empty_raises():
    # граница: pop из пустого стека
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()


def test_stack_peek_empty_raises():
    # граница: peek из пустого стека
    s = Stack()
    with pytest.raises(IndexError):
        s.peek()


def test_stack_single_element():
    # граница: один элемент
    s = Stack()
    s.push(42)
    assert s.peek() == 42
    assert s.pop() == 42
    assert s.is_empty() is True


def test_stack_interleaved_push_pop():
    # нетривиальный: чередование push/pop
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    s.push(3)
    s.push(4)
    assert s.pop() == 4
    assert s.pop() == 3
    assert s.pop() == 1


# --- Queue ---


def test_queue_empty_initially():
    # граница: новая очередь пуста
    q = Queue()
    assert q.is_empty() is True
    assert q.size() == 0


def test_queue_enqueue_dequeue_fifo():
    # типичный: FIFO — первый добавленный выходит первым
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.peek() == 1
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.is_empty() is True


def test_queue_size_after_operations():
    # типичный: size отражает число элементов
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    assert q.size() == 2
    q.dequeue()
    assert q.size() == 1


def test_queue_dequeue_empty_raises():
    # граница: dequeue из пустой очереди
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()


def test_queue_peek_empty_raises():
    # граница: peek из пустой очереди
    q = Queue()
    with pytest.raises(IndexError):
        q.peek()


def test_queue_single_element_clears_tail():
    # граница: после удаления единственного элемента очередь снова пуста
    q = Queue()
    q.enqueue(7)
    assert q.dequeue() == 7
    assert q.is_empty() is True
    q.enqueue(8)
    assert q.peek() == 8
    assert q.dequeue() == 8


def test_queue_interleaved_enqueue_dequeue():
    # нетривиальный: чередование enqueue/dequeue
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    q.enqueue(3)
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.is_empty() is True
