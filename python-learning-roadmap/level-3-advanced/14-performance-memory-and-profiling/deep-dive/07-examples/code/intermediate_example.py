from time import perf_counter
start = perf_counter()
result = sum(number * number for number in range(1_000_000))
print(result, perf_counter() - start)
