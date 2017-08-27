# Generator Function in Python: Better Utilization of Memory


# Declare Function is Python usin 'def'
def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True


# Generator Function Use Yield, and
# next time it start from the same nth position onwards
def primes(n=1):
    while True:
        if isprime(n):
            yield n
        n += 1


for n in primes():
    if n > 100:
        break
    print(n)
