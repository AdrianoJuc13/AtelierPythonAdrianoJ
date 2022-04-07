def your_function(*address):
    total_sum = 0
    for i in address:
        # print(type(i))
        if type(i) == int:
            total_sum += i
    return total_sum


if __name__ == '__main__':
    print(your_function(1, 5, -3, "abc", [12, 56, "cad"]))
