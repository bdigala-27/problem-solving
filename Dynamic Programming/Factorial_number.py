import time

def factorial(n): #memoization
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] * i
    return dp[n]

def factorial2(n):
    if n==0 or n==1:
        return 1
    else:
        return (n*factorial(n-1))

start_time = time.time() * 1000  # Start time in milliseconds
n = 2000
print(factorial(n))
end_time = time.time() * 1000  # End time in milliseconds

execution_time = end_time - start_time
print("Execution time:", execution_time, "milliseconds")
