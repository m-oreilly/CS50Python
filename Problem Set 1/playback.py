# Main
def main():
    x = get_user_input()
    x = slow_playback(x)
    print(f"{x}")


# Returns user input as str
def get_user_input():
    return input("What would you like me to slow down? ").strip()


# Returns input in lowercase
def slow_playback(slow):
    return slow.replace(" ", "...")


main()
