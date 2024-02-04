from main import *
import math

def test_simple_work():
	""" done. """
	assert work_calc(10, 2, 2) == 50.0
	assert work_calc(20, 3, 2) == 415.625
	assert work_calc(30, 4, 2) == 1890.0
	assert work_calc(40, 5, 8) == 1890.0
	assert work_calc(50, 2, 1) == 1890.0
	assert work_calc(21, 4, 20) == 1890.0

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 25.0
	assert work_calc(20, 1, 2, lambda n: n*n) == 272.875
	assert work_calc(30, 3, 2, lambda n: n) == 348.8125
	assert work_calc(40, 2, 1, lambda n: n) == 348.8125
	assert work_calc(21, 4, 2,lambda n: 1) == 25.0
	assert work_calc(40, 2, 4, lambda n: n*n) == 272.875


def test_compare_work():
    a = 2
    b = 2
    sizes = [10, 20, 50, 100, 500, 1000]

    # Case: f(n) = 1
    def work_fn1(n):
        return span_calc(n, a, b, lambda x: 1)

    def work_fn2(n):
        return n

    print("Results for f(n) = 1:")
    result_1 = compare_work(work_fn1, work_fn2, sizes)
    print(result_1)

    # Case: f(n) = log(n)

    def work_fn3(n):
        return span_calc(n, a, b, math.log)

    def work_fn4(n):
        return n * math.log(n)

    print("\nResults for f(n) = log(n):")
    result_log = compare_work(work_fn3, work_fn4, sizes)
    print(result_log)

    # Case: f(n) = n
    def work_fn5(n):
        return span_calc(n, a, b, lambda x: x)

    def work_fn6(n):
        return n**2

    print("\nResults for f(n) = n:")
    result_n = compare_work(work_fn5, work_fn6, sizes)
    print(result_n)




def test_compare_span(span_func1, span_func2, max_n):
    for n in range(1, max_n + 1):
        result1 = span_func1(n)
        result2 = span_func2(n)
        assert result1 == result2, f"Mismatch for n={n}: Span 1: {result1}, Span 2: {result2}"

    print("All tests passed.")
    return True

