import io

from tracer import tracer


def test_factorial_trace_shape():
    # типичный: факториал
    buf = io.StringIO()

    @tracer(file=buf)
    def fact(n: int) -> int:
        if n <= 1:
            return 1
        return n * fact(n - 1)

    assert fact(3) == 6
    text = buf.getvalue()
    lines = [ln for ln in text.strip().splitlines() if ln]

    assert lines[0] == "-> fact(3)"
    assert "  -> fact(2)" in lines
    assert "    -> fact(1)" in lines
    assert "    <- fact = 1" in lines
    assert "  <- fact = 2" in lines
    assert lines[-1] == "<- fact = 6"


def test_depth_indent_grows_and_shrinks():
    # граница: глубина 0 → 1 → 2 → 1 → 0
    buf = io.StringIO()

    @tracer(file=buf)
    def f(n: int) -> int:
        if n == 0:
            return 0
        return f(n - 1) + 1

    assert f(2) == 2
    lines = buf.getvalue().splitlines()

    assert lines[0].startswith("->")
    assert lines[1].startswith("  ->")
    assert lines[2].startswith("    ->")
    assert lines[3].startswith("    <-")
    assert lines[4].startswith("  <-")
    assert lines[5].startswith("<-")


def test_base_case_single_call():
    # граница: один вызов без рекурсии
    buf = io.StringIO()

    @tracer(file=buf)
    def identity(x):
        return x

    assert identity(42) == 42
    assert buf.getvalue() == "-> identity(42)\n<- identity = 42\n"


def test_kwargs_and_multiple_args():
    # нетривиальный: позиционные + именованные аргументы в логе
    buf = io.StringIO()

    @tracer(file=buf)
    def add(a, b=0):
        return a + b

    assert add(1, b=2) == 3
    text = buf.getvalue()
    assert "-> add(1, b=2)" in text
    assert "<- add = 3" in text


def test_exception_still_unwinds_depth():
    # граница: исключение не ломает счётчик глубины для следующих вызовов
    buf = io.StringIO()

    @tracer(file=buf)
    def f(n: int, explode: bool = False) -> int:
        if explode and n == 0:
            raise ValueError("stop")
        if n == 0:
            return 0
        return f(n - 1, explode=explode) + 1

    try:
        f(1, explode=True)
    except ValueError:
        pass

    buf.seek(0)
    buf.truncate(0)

    assert f(1) == 1
    # отступ снова с нуля
    lines = buf.getvalue().splitlines()
    assert lines[0] == "-> f(1)"
    assert lines[-1] == "<- f = 1"


def test_decorator_preserves_name():
    # граница: functools.wraps сохраняет __name__
    @tracer
    def fib(n):
        return n

    assert fib.__name__ == "fib"


def test_bare_at_tracer_works():
    # типичный: @tracer без скобок
    buf = io.StringIO()

    import sys

    old = sys.stdout
    sys.stdout = buf
    try:

        @tracer
        def g(n):
            if n == 0:
                return 0
            return g(n - 1)

        assert g(1) == 0
    finally:
        sys.stdout = old

    assert "-> g(1)" in buf.getvalue()
    assert "<- g = 0" in buf.getvalue()
