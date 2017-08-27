# While Loop in Python

# Example 01: Simple While Counter
count = 0

while count < 9:
    print('The count is:', count)
    count = count + 1

# Divider Line
print('========================')

# Example 02: Nested Loop: Find Prime Numbers

i = 2
while i < 100:
    j = 2

    while j <= (i / j):
        if not (i % j):
            break
        j = j + 1

    if j > (i / j):
        print(i, " is prime")
    i = i + 1
