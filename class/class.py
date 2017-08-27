# Class in Python: Reusing code and data with calss.


# Declare a class using the 'class' keyword
class Fibonacci():
    # __init__ is a constructor and will initialized as soon as
    # instance of the class is created.
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def series(self):
        while True:
            yield (self.b)
            self.a, self.b = self.b, self.a + self.b


# Create an instance of the Fibonacci Class
f = Fibonacci(0, 1)

# Print the Fibonacci Series below 100
for r in f.series():
    if r > 100:
        break
    print(r, end=' ')
