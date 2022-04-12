def main():
    # Initialise variable
    x = None

    # Start loop, to repeat until correct answer is given
    while check_for_equality(x) is False:
        x = great_question_answer()
        x = clean_up_answer(x)
        if check_for_equality(x) is True:
            print("Yes")
        else:
            print("No")



# Ask the great question
def great_question_answer():
    return input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")


# Clean up user input
def clean_up_answer(dirty_answer):
    return dirty_answer.strip().replace("-", " ").lower()


# Check for equality
def check_for_equality(clean_answer):
    if clean_answer == "42":
        return True
    elif clean_answer == "forty two":
        return True
    else:
        return False


# Call main to run
main()
