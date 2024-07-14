import math

n = 150
L = [1, 3]  # Starting values for the Fibonacci sequence

def fib(n, I):
    L = list(I)
    L.append((L[0]+L[1]) % n)
    current = [L[1],L[2]]
    count = 1
    while current != [L[0],L[1]]:
        L.append((current[0]+current[1])%n)
        current = [current[1],(current[0]+current[1])%n]
        count += 1
    return L      

# Generate Fibonacci numbers
fibseq = fib(7, [0,1])
print(fibseq)

''' Convert the list to a DataFrame and write to a CSV file
df = pd.DataFrame(fibonacci_sequence, columns=['Fibonacci Number'])
df.to_csv('fibonacci_sequence.csv', index=False)

print("Fibonacci sequence has been written to fibonacci_sequence.csv.")
'''

