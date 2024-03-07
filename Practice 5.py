# Task 1
def sumN(n):
    return sum((i for i in range(1, n+1)))

def sumNCubes(n):
    return sum((i**3 for i in range(1, n+1)))

print(sumN(10))
print(sumNCubes(10))

# Task 2
def fibbonacci(n):
    if n < 0:
        print("Incorrect input")
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibbonacci(n-1) + fibbonacci(n-2)

print(fibbonacci(5))

# Task 3
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

print(factorial(5))