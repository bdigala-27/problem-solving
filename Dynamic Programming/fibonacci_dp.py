import time
# '''
def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		table = [0] * (n + 1)
		table[0] = 0
		table[1] = 1
		for i in range(2, n+1):
			table[i] = table[i-1] + table[i-2]
		return table[n]
# '''
# def fibonacci(n, cache={}):
# 	if n in cache:
# 		return cache[n]
# 	if n == 0:
# 		result = 0
# 	elif n == 1:
# 		result = 1
# 	else:
# 		result = fibonacci(n-1) + fibonacci(n-2)
# 	cache[n] = result
# 	return result


start_time = time.time() * 1000  # Start time in milliseconds
n = 950
print(fibonacci(n))
end_time = time.time() * 1000  # End time in milliseconds

execution_time = end_time - start_time
print("Execution time:", execution_time, "milliseconds")
