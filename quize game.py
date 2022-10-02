#-------------------------------
def new_game():
    guesses=[]
    correct_gusses = 0
    question_num =1

    for key in questions:
        print("-------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess=input('Enter (A,B,C,D) :')
        guess=guess.upper()
        guesses.append(guess)

        correct_gusses += check_answer(questions.get(key),guess)
        question_num+=1

    display_score(correct_gusses,guesses)

#-------------------------------
def check_answer(answer,guess):
    if answer==guess:
        print('CORRECT!')
        return 1
    else:
        print('WRONG!')
        return 0
#-------------------------------
def display_score(correct_gusses,guesses):
    print("-------------------------------")
    print("RESULT")
    print("-------------------------------")
    print("ANSWER  :",end=' ')
    for i in questions:
        print(questions.get(i),end=' ')
    print()

    print("GUESSES :", end=' ')
    for i in guesses:
        print(i, end=' ')
    print()


    score=int((correct_gusses/len(questions))*100)
    print('Your score is :',score,'%')

#-------------------------------
def play_again():
    respons=input('Do you want to play again?(yes,No):').upper()
    if respons=="YES":
        return True
    else:
        return False



#-------------------------------


questions={"1) what is the heightest mountain in the world? :":"A",
"2) what year was python created? :":"B",
"3) who is the founder of face book :":"C",
"4) when is friendship Day :":"A"}


options=[['A . Everest ','B . Piduruthalagala','C . Denail','D . Mount logan'],
          ['A . 1989','B . 1991','C . 2000','D.  2016'],
          ['A . Elon Musk' ,'B . Bill Gates ','C . Mark Zuckerberg','D . Guido van Rossum '],
           ['A . July 30','B . September 30','C . Octomber 30','D . November 30 ']]


new_game()

while play_again():
    new_game()

print('BYE!.........')
