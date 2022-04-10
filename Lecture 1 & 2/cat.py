def main():
    number = get_number()
    meow(number)


def meow(n):
    for _ in range(n):
        print("Meow")


def get_number():
    while True:
        n = int(input("What is N? "))
        if n > 0:
            return n


main()
