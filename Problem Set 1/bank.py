def main():
    # Define variables for use in functions - improves future customization of redress amounts and greetings
    ok_greeting = "h"
    good_greeting = "hello"
    large_redress = 100
    small_redress = 20
    no_redress = 0

    # Teller gives their greeting
    tellers_greeting = ask_for_greeting()

    # Passes in the tellers greeting to be checked and if true prints appropriate redress amount
    # Else returns false and provides the large redress
    # Could improve formatting in future with {variable:.2f}
    if check_for_good_greeting(tellers_greeting, good_greeting):
        print(f"${no_redress}")
    elif check_for_ok_greeting(tellers_greeting, ok_greeting):
        print(f"${small_redress}")
    else:
        print(f"${large_redress}")


# Ask user to give a greeting, removes leading spaces removed, sets lower case and returns
def ask_for_greeting():
    return input("Greeting: ").lower().lstrip()


# Returns true if greeting begins with a good greeting
def check_for_good_greeting(greeting, good_greeting):
    return greeting.startswith(good_greeting)


# Returns true if greeting begins with an ok greeting
def check_for_ok_greeting(greeting, ok_greeting):
    return greeting.startswith(ok_greeting)


main()
