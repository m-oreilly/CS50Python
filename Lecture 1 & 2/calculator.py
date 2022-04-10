def main():
    x = int(input("What is x? "))
    print(f"X Squared is", square(x))


def square(n):
    return pow(n, 2)


main()
