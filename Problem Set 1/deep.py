def main():

    # Start loop, to repeat until correct answer is given
    while True:
        users_guess = answer_to_great_question()

        if check_for_equality(users_guess):
            print("Yes")
            break
        else:
            print("No")


# Ask the great question
def answer_to_great_question():
    return input("What is the Answer to the Great Question of Life, "
                 "the Universe, and Everything? ").strip().replace("-", " ").lower()


# Check for equality
def check_for_equality(guess):
    return guess == "42" or guess == "forty two"


# Call main to run
main()
