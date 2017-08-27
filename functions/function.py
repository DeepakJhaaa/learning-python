# Function in Python: Reusing the Code

# Declare Funtion is Python usin 'def'
def isprime(n):
    if n == 1:
        print(n, 'is a special number.')
        return False
    for x in range(2, n):
        if n % x == 0:
            print("{} equal {} X {}".format(n, x, n / x))
            return False
    else:
        print(n, " is a Prime Number.")
        return True


# Reuse of the created Function
for x in range(2, 25):
    isprime(x)
