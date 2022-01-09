def fibonacci_nums(n):
  if n <= 0:
    return [0]
  sequence = [0, 1]
  while len(sequence) <= n:
    next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
    sequence.append(next_value)
  return sequence
print("First 7 Fibonacci numbers:")
print(fibonacci_nums(7))
print("\nFirst 15 Fibonacci numbers:")
print(fibonacci_nums(15))
print("\nFirst 50 Fibonacci numbers:")
print(fibonacci_nums(50))
