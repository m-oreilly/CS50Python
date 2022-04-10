def main():
    c = 300000000
    m = get_user_input()
    e = calc_joules(m, c)
    # Print the Joules back to the user
    print("E:", e)


# Get the users input
def get_user_input():
    return int(input("m: "))


# Calculate the Joules
def calc_joules(mass, speedoflight):
    return mass * (speedoflight ** 2)


main()
