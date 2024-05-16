import pandas as pd
import math

n = 150
L = [1, 3]  # Starting values for the Fibonacci sequence

def fib(k, I):
    L = list(I)
    while len(L) < k:  # Ensure we generate exactly k numbers
        L.append(L[-2] + L[-1])
    return L


# Generate Fibonacci numbers
fibonacci_sequence = fib(n, L)

# Convert the list to a DataFrame and write to a CSV file
df = pd.DataFrame(fibonacci_sequence, columns=['Fibonacci Number'])
df.to_csv('fibonacci_sequence.csv', index=False)

print("Fibonacci sequence has been written to fibonacci_sequence.csv.")


