def main():

    # Start loop, to repeat until correct answer is given
    while True:
        users_answer = great_question_answer()

        if check_for_equality(users_answer):
            print("Yes")
            break
        else:
            print("No")


# Ask the great question
def great_question_answer():
    return input("What is the Answer to the Great Question of Life, "
                 "the Universe, and Everything? ").strip().replace("-", " ").lower()


# Check for equality
def check_for_equality(clean_answer):
    return clean_answer == "42" or clean_answer == "forty two"


# Call main to run
main()
