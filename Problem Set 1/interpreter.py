def main():
    x, y, z = get_expression()
    answer = calc_expression(x, y, z)
    print(float(answer))


def get_expression():
    return input("Expression: ").split()


def calc_expression(x, y, z):
    x = int(x)
    z = int(z)
    if y == "+":
        answer = x + z
    elif y == "-":
        answer = x - z
    elif y == "*":
        answer = x * z
    else:
        answer = x / z
    return answer


main()
