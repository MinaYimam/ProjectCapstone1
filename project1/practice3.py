""" A quiz program. """
"""creating dictionaries
funtion"""
artsdict = {"Who painted the Mona Lisa?": ["Leonardo da vinci"],
            "What precious stone is used to make the artist\'s pigment ultramarine?": ["Lapiz lazuli"],
            "Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?": ["chicago"]}
spacedict = {"Which planet is closest to the sun?": "Mercury",
            "Which planet spins in the opposite direction to all the others in the solar system?": "Venus",
              "How many moons does Mars have?" : '2'}
#print(dictionary)


def main():
    question = input('Would you like art or space question?')
    validate_answer(question)
   ##print(f"you choose {validated_answer}, here are your questions:  ")

    print('End of quiz!')
    print(f'Your total score on art questions is {total_score} out of 3.')


def validate_answer(question):
    #total_score = 0
    if question.casefold() == 'art':
        print(f"you choose {question}, here are your questions:  ")
        for key in artsdict:
            print(key)
            answer1 = input('enter your answers and press enter: ')
            art_answer(answer1)
    elif question.casefold() == 'space':
        print(f"you choose {question}, here are your questions:  ")
        for key, value in spacedict.items():
            print(key)
            answer2 = input('enter your answer and press enter: ')
            space_answer(answer2)
    else:
        while question.casefold() != 'art' or 'space':
            print('This is not a valid topic!')
            return main()

            #return main
    for value in artsdict.values():
        print(value)


def art_answer(answer1):
    x = [value[i] for value in artsdict.values() for i in range(1)]
    if answer1.casefold() == x:
            print(x)
    elif answer1.casefold() != x[2]:
            print(x[2])
    elif answer1.casefold() != x[3]:
            print(x[1])
    """
    for key, value in artsdict.items():
        while key not in value : True
        return print(f"wrong the answer is{value} ")
for value in artsdict.values():
        print('wrong, the answer is')
        print(artsdict[value])
        """
   # total_score +=1
        #else:
           # print(f'the answer is {value}')
            #return


        #while answer1.casefold() not in artsdict.values():
           # for value in artsdict.values():
             #   print(f'the answer is {value}')
            #return
"""if answer1 == artsdict.values():
            print('correct!')
        else:
            return
"""


def space_answer(answer2, total_score=0):
    for values in artsdict.values():
        while answer2.casefold() not in spacedict.values():
            for item, value in spacedict.values():
                print(item, value)
                print(f'wrong answer, the answer is {value}')
            return
        if answer2 == values:
            print('Correct!')
            total_score +=1


main()



    #total_score = 0




   # for key, value in s\():
     #   print(f'topics:{key}')
   # question = input('Would you like art or space question')
    #validate_question = validate_q(question)
   # print(f"you choose {validate_question}, here are your questions:  ")

#for key, value in artsdict.items():
#    print(f'topics:{value}')
"""def main():
    total_score = 0
    for key, value in dictionary1.items():
        print(f'topics:{key}')
    question = input('Would you like art or space question')
    validate_question = validate_q(question)
    print(f"you choose {validate_question}, here are your questions:  ")

    if validate_question == 'art':
        for i in dictionary1["art"]:
            print(i)
            answers = input('enter your answer  ')
            if answers == dictionary1(value):
                print('correct')
                total_score +=1

    else:
        return

    #print(input(dictionary[validate_question]["aq1"][0]))
    for i in dictionary:
        print(i)
        print(input('enter your answers?'))
    if validate_q == dictionary["art"]:
        for key, value in dictionary.keys():
            print(value)
def check_answers(answer):
    if answer == dictionary1():
        return "good job"
    else:
        f'you answered wrong the, the answer is {dictionary1()} 
def validate_q(question):
    while question not in dictionary1.keys():
        for key, value in dictionary1.items():
            print(key)
        question = input('You can only choose one of the topics?')

        #question = input('Would you like art or space question?')
    else:
        return question


main()
"""
