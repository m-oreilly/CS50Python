def main():
    # Set c for the speed of light
    c = 300000000

    # Ask for Mass, Calculate energy
    m = get_mass()
    e = calc_joules(m, c)

    # Print the Energy back to the user
    print("E:", e)


# Get the users input
def get_mass():
    return int(input("m: "))


# Returns Energy, takes in Mass and Speed of light
def calc_joules(mass, speed_of_light):
    return mass * (speed_of_light ** 2)


main()
