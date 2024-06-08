def lower_triangular_pattern(n):
    for i in range(1, n + 1):
        print('*' * i)

n = int(input('Enter a value for lower triangle''\n'))
lower_triangular_pattern(n)

def upper_triangular_pattern(n1):
    for i in range(n1, 0, -1):
        print('*' * i)

n1 = int(input('Enter a value for upper triangle''\n'))
upper_triangular_pattern(n1)

def pyramid_pattern(n2):
    for i in range(1, n2 + 1):
        print(' ' * (n2 - i) + '*' * (2 * i - 1))

n2 = int(input('Enter a value for pyramid pattern''\n'))
pyramid_pattern(n2)
