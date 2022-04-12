def main():
    the_great_question = "What is the Answer to the Great Question of Life, the Universe, and Everything? "
    the_answers = ["42", "forty two"]

    # Start loop, to repeat until correct answer is given
    while True:
        users_guess = get_answer_to_great_question(the_great_question)

        if check_guess(users_guess, the_answers):
            print("Yes")
            break
        else:
            print("No")


# Ask the great question
def get_answer_to_great_question(question):
    return input(question).strip().replace("-", " ").lower()


# Check for equality
def check_guess(guess, answer):
    return guess in answer


# Call main to run
main()
