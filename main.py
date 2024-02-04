"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###

def simple_work_calc(n, a, b):
	# TODO
	pass

	if n <= 1:
		return n
	else:
		return a * simple_work_calc(n / b, a, b) + n












def work_calc(n, a, b, f):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	pass
	if n <= 1:
		return n
	else:
		return a * work_calc(n / b, a, b, f) + f(n)
	
print(simple_work_calc(21, 4, 20))










def span_calc(n, a, b, f):
	if n == 1:
		return f(1)
	k = 1
	current_work = f(n)
	subproblem_sizes = [n // b] * (b - 1) + [n - (n // b) * (b - 1)]
	subproblem_spans = [span_calc(size, a, b, f) for size in subproblem_sizes]
	max_subproblem_span = max(subproblem_spans)
	return current_work + a * max_subproblem_span


def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result






def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	results = []

	for size in sizes:
		span1 = span_fn1(size)
		span2 = span_fn2(size)
		results.append((size, span1, span2))
	return results
	