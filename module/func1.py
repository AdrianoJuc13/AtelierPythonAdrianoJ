
def sum_n(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum


def sum_even(n):
    sum = 0
    for i in range(0, n+1, 2):
        sum += i
    return sum


def sum_odd(n):
    sum = 0
    for i in range(1, n+1, 2):
        sum += i
    return sum

