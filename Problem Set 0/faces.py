def main():
    x = get_user_input()
    x = covert(x)
    print(f"{x}")


# Returns user input as str
def get_user_input():
    return input("Please type something, I'll update text faces.py with happy and sad smileys for you!  ")


# Returns input with smiley faces.py converted
def covert(faces):
    return faces.replace(":)", "🙂").replace(":(", "🙁")


# Run Main
main()
