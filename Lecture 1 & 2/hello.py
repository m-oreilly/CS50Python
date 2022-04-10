def main():
    name = input("What is your name? ").strip().title()
    hello(name)


def hello(to="world"):
    print(f"Hello, {to}")


main()
