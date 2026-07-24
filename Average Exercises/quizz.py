#---------------------------------------------------------------#
#                           Quizz Game                          #
#---------------------------------------------------------------#

# We are going to create different question and giving propoisions

#---------------------------------------------------------------#
#                           Variables                           #
#---------------------------------------------------------------#

questions = ("How many days are in a day ?" ,
             "How many planets are in our solar system ?" ,
             "24/6 = "                                     )


possibilites = (("A. 7", "B. 4", "C. 6"),
                ("A. 8", "B. 7", "C. 14"),
                ("A. 5", "B. 6", "C. 4"))

answer =        ("A", "A", "C")

guesses =       []

score = 0

question_number = 0

for question in questions :
    printed_number = question_number + 1
    print("-----------------------------------")
    print(f"Question {printed_number}")
    print(question)
    for option in possibilites[question_number]:
        print(option)

    guess = input("Enter the letter corresponding to your answer : ").upper()   
    while guess != "A" and guess != "B" and guess != "C" :
        guess=input("Please enter a correct value : ").upper()
    guesses.append(guess)
    if guess == answer[question_number] :
        print("You got this right !")
        score += 1
    else :
        print("Wrong answer...")
    question_number+= 1


print(f"You got {score} points out of {len(questions)}")


