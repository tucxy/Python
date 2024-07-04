import numpy as np

def fibonacci_modulo_p_cycles(p):
    def find_cycle(a, b, mod):
        sequence = [(a, b)]
        seen = {(a, b): 0}
        index = 0
        while True:
            next_fib = (sequence[-1][0] + sequence[-1][1]) % mod
            new_pair = (sequence[-1][1], next_fib)
            index += 1
            if new_pair in seen:
                cycle_start = seen[new_pair]
                cycle = sequence[cycle_start:]
                return cycle
            seen[new_pair] = index
            sequence.append(new_pair)

    cycle_lengths = []
    visited = set()

    for a in range(p):
        for b in range(p):
            if (a, b) not in visited:
                cycle = find_cycle(a, b, p)
                cycle_length = len(cycle)
                cycle_lengths.append(cycle_length)
                # Mark all pairs in this cycle as visited
                for pair in cycle:
                    visited.add(pair)

    return cycle_lengths

# Parameters
p = 101  # Modulus

# Calculate the lengths of all unique cycles
cycle_lengths = fibonacci_modulo_p_cycles(p)

# Display the results
print(f"Cycle lengths for p = {p}: {cycle_lengths}")
print(f"Number of cycles: {len(cycle_lengths)}")
print(f"Sum of all cycle lengths: {sum(cycle_lengths)}")
print(f"Largest cycle length: {max(cycle_lengths)}")


def matrix_mult(A, B, mod):
    """Multiplies two 2x2 matrices A and B under modulo mod."""
    return np.array([
        [(A[0,0] * B[0,0] + A[0,1] * B[1,0]) % mod, (A[0,0] * B[0,1] + A[0,1] * B[1,1]) % mod],
        [(A[1,0] * B[0,0] + A[1,1] * B[1,0]) % mod, (A[1,0] * B[0,1] + A[1,1] * B[1,1]) % mod]
    ])

def matrix_power(matrix, power, mod):
    """Raises the matrix to the given power under modulo mod using exponentiation by squaring."""
    result = np.identity(2, dtype=int)
    base = matrix

    while power > 0:
        if power % 2 == 1:
            result = matrix_mult(result, base, mod)
        base = matrix_mult(base, base, mod)
        power //= 2

    return result

def fibonacci_matrix_power(n, mod):
    """Calculates the n-th power of the Fibonacci matrix under modulo mod."""
    if n == 0:
        return np.identity(2, dtype=int) % mod

    F = np.array([[1, 1],
                  [1, 0]], dtype=int)

    F_n = matrix_power(F, n, mod)
    return F_n

# Example usage
n = 42
mod = 211
result_matrix = fibonacci_matrix_power(n, mod)
print(f"The {n}-th power of the Fibonacci matrix modulo {mod} is:\n{result_matrix}")

distinctlengths = [1]

for length in cycle_lengths:
    for dlength in distinctlengths:
        if length != dlength:
            distinctlengths.append(length)
print(f"Distinct lengths = {distinctlengths}")