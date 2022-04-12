def main():
    # Define variables to improve reuse of codebase
    the_great_question = "What is the Answer to the Great Question of Life, the Universe, and Everything? "

    # Start loop, to repeat until correct answer is given
    while True:
        users_guess = answer_to_great_question(the_great_question)

        if check_for_equality(users_guess):
            print("Yes")
            break
        else:
            print("No")


# Ask the great question
def answer_to_great_question(question):
    return input(question).strip().replace("-", " ").lower()


# Check for equality
def check_for_equality(guess):
    return guess == "42" or guess == "forty two"


# Call main to run
main()
