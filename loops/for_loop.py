# For Loop in Python

# First Example: All Letters of a String
for letter in 'Python':
    print('Current Letter :', letter)

# Divider Line
print('========================')

# Second Example: Print Elements of an Array
fruits = ['banana', 'apple', 'mango']

for fruit in fruits:
    print('Current fruit :', fruit)

# Divider Line
print('========================')

# Third Example: Continue Statement
for letter in 'Python':
    if letter == 'h':
        continue
    print('Current Letter :', letter)

var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print('Current variable value :', var)

# Divider Line
print('========================')

# Third Example: PASS Statement
for letter in 'Python':
    if letter == 'h':
        pass
        print('This is pass block')

    print('Current Letter :', letter)

# Divider Line
print('========================')

# Fourth Example: Read lines from the file
fh = open('lines.txt')
for line in fh.readlines():
    print(line)
