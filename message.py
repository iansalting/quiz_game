import random


def newgame():
    correct_guesses = 0
    guesses = []
    question_num = 1

    for key in questions:
        print("---------------------------")
        print(key)
        for i in option[question_num-1]:
            print(i)
        guess = input("Enter (A.B.C.D) ").lower()
        #guess = guess.lower()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses, guesses)



def check_answer(answer, guesses):
    if answer == guesses:
        print("Correct!!")
        return 1
    else:
        print("Wrong!!")
        return 0
def display_score(correct_guesses, guesses):
    print("---------------------------")
    print("Result")
    print("---------------------------")
    print("Answer")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your Score is :" + str(score))
def play_again():
    again = input("Play Again? Y/N ").upper()
    if again == "Y":
        return True
    else:
        return False 

questions = {"What is 1+1? " : "a",
            "WHat is 2+2? " : "b",
            "What is 4+4? " : "c"
            }

option = [["a = 2", "b = 1", "c = 3"],
          ["a = 2", "b = 4", "c = 5"],
          ["a = 3", "b = 5", "c = 8"]
          ]

newgame()
while play_again():
    newgame()