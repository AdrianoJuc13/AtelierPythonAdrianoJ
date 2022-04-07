import module.func1 as functions


def your_function(*args, **kwargs):
    total_sum = 0
    for i in args:
        # print(type(i))
        if type(i) == int:
            total_sum += i
    return total_sum


def is_integer():
    x = input("Request a value: ")
    try:
        x = int(x)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    print(your_function(1, 5, -3, "abc", [12, 56, "cad"]))
    print(your_function())
    print(your_function(2, 4, "abc", param_1=3))

    # while True:
    print(is_integer())

    n = 10
    print("suma tuturor numerelor de la [0, n] = ", functions.sum_n(n))
    print("suma numerelor pare de la [0, n] = ", functions.sum_even(n))
    print("suma numerelor impare de la [0. n] = ", functions.sum_odd(n))
