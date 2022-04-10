def main():
    score = int(input("What was the students score? "))

    if score >= 90:
        print(f"A score of {score} is Grade A.")
    elif score >= 80:
        print(f"A score of {score} is Grade B.")
    elif score >= 70:
        print(f"A score of {score} is a Grade C.")
    elif score >= 60:
        print(f"A score of {score} is a Grade D.")
    else:
        print(f"A score of {score} is an F. You failed.")

main()
