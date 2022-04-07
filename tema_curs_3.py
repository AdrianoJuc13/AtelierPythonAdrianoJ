def your_function(x):
    sum = 0
    for i in x:
        if type(i) == int:
            sum += i
    return sum


if __name__ == '__main__':
    x = 1, 5, -3, "abc", [12, 56, "cad"]
    print(your_function(x))
