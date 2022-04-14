# Program will ask user to for time (12/24 hr format)
# Will confirm if it's a meal time,  7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00
# If not a meal time, end program

# Main
def main():
    users_time = ask_for_the_time()
    converted_time = convert(users_time)
    meal = is_it_meal_time(converted_time)
    if meal is not None:
        print(meal)


# Ask question and returns formatted users answer
def ask_for_the_time():
    return input("What time is it? ").lower().strip().replace(".", "").replace(" ", ":")


# Takes in time in 12, or 24 hr formats and returns time as float
def convert(time):
    if time.endswith("am"):
        hours, minutes, am = time.split(":")
    elif time.endswith("pm"):
        hours, minutes, pm = time.split(":")
        hours = float(hours) + 12
    else:
        hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) / 60
    converted_time = hours + minutes
    return converted_time


# Takes in time as float, returns if its breakfast, lunch, or dinner
def is_it_meal_time(time_to_check):
    if 7 <= time_to_check <= 8:
        return "breakfast time"
    elif 12 <= time_to_check <= 13:
        return "lunch time"
    elif 18 <= time_to_check <= 19:
        return "dinner time"
    else:
        return None


if __name__ == "__main__":
    main()
