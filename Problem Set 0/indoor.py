# Main
def main():
    x = get_user_input()
    x = indoor_voice(x)
    print(f"{x}")


# Returns user input as str
def get_user_input():
    return input("What shall we say with our indoor.py voice?: ")


# Returns input in lowercase
def indoor_voice(indoor):
    return indoor.lower()


main()
