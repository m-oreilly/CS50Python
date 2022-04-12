def main():
    greeting = ask_for_greeting()

    # Passes in greeting to be checked and if true prints appropriate redress amount
    if check_greeting_for_hello(greeting):
        print("$0")
    elif check_greeting_for_h(greeting):
        print("£20")
    else:
        print("$100")


# Ask user to give a greeting, returns with lower case, leading spaces removed
def ask_for_greeting():
    return input("Greeting: ").lower().lstrip()


# Returns true if greeting begins with hello
def check_greeting_for_hello(to_check):
    return to_check.startswith("hello")


# Returns true if greeting begins with h
def check_greeting_for_h(to_check):
    return to_check.startswith("h")


main()
