def main():
    greeting = ask_for_greeting()
    if check_greeting_for_hello(greeting):
        print("$0")
    elif check_greeting_for_h(greeting):
        print("£20")
    else:
        print("$100")


def ask_for_greeting():
    return input("Greeting: ").lower().lstrip()


def check_greeting_for_hello(to_check):
    return to_check.startswith("hello")


def check_greeting_for_h(to_check):
    return to_check.startswith("h")


main()
