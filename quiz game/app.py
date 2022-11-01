def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions = {
 "karkinos healthcare works on?: ": "A",
 "karkinos healthcare main head quaters?: ": "B",
 "how many types of cancers are there: ": "C",
 "how many tyes of cancers can cure  karkinos health care?: ": "A"
}

options = [["A. cancer disease", "B. heart disease", "C. eye disease", "D. brain disease"],
          ["A. banglore", "B. mumbai", "C. hyderabad", "D. delhi"],
          ["A. more than 25", "B. more than 50", "C. more than 100", "D. more than 150"],
          ["A. 6","B. 3", "C. 2", "D. 7"]]

new_game()

while play_again():
    new_game()

print("KARKINOS HEALTHCARE PRIVATE LIMITED")