# If up for a challenge, optionally add support for 12-hour times,
# allowing the user to input times in these formats too:
# #:## a.m. and ##:## a.m.
# #:## p.m. and ##:## p.m.
#  7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.

what_time = "What time is it? "
breakfast = "breakfast time"
lunch = "lunch time"
dinner = "dinner time"


def main():
    while True:
        time = ask_for_the_time(what_time)
        converted_time = convert(time)
        meal = which_meal_time(converted_time)
        if meal is not None:
            print(meal)


def ask_for_the_time(question):
    return input(question).lower().strip().replace(".", "").replace(" ", ":")


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


def which_meal_time(time_to_check):
    if 7 <= time_to_check <= 8:
        return breakfast
    elif 12 <= time_to_check <= 13:
        return lunch
    elif 18 <= time_to_check <= 19:
        return dinner
    else:
        return None


if __name__ == "__main__":
    main()
