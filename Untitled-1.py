import math

def span_calc(n, a, b, f):
    if n == 1:
        return f(1)
    k = 1
    current_work = f(n)
    subproblem_sizes = [n // b] * (b - 1) + [n - (n // b) * (b - 1)]
    subproblem_spans = [span_calc(size, a, b, f) for size in subproblem_sizes]
    max_subproblem_span = max(subproblem_spans)
    return current_work + a * max_subproblem_span

def f_constant(x):
    return 1

def f_logarithmic(x):
    return math.log(x)

def f_linear(x):
    return x

def run_examples():
    examples = [
        {'f': f_constant, 'name': 'Constant', 'color': 'blue'},
        {'f': f_logarithmic, 'name': 'Logarithmic', 'color': 'green'},
        {'f': f_linear, 'name': 'Linear', 'color': 'red'},
    ]

    n_values = [16, 32, 64]  # Adjust as needed
    a = 2
    b = 2

    for example in examples:
        f_func = example['f']
        name = example['name']
        color = example['color']

        print(f"\nExample for f(n) = {name}:")

        for n in n_values:
            result = span_calc(n, a, b, f_func)
            print(f"Span for n={n}: {result} (Color: {color})")

if __name__ == "__main__":
    run_examples()