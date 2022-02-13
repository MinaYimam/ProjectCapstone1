""" A quiz program. """
"""THIS IS A DICTIONARY HOLDING A QUESTION AND AN ANSWER OF ART AND SPACE QUESTION
THE USER WILL BE ASKED IF THEY WANT AN ART OR A SPACE QUESTION AND BASED ON THEIR INPUT THIS FUNCITON WILL IDENTIFY IF 
THE USER ANSWERED CORRECT OR NOT AND WILL SHOW HOW MANY CORRECT ANSWER THEY GOT FROM THE WHOLE QUESTION"""


art_dict = {"Who painted the Mona Lisa?": "Leonardo da vinci",
            "What precious stone is used to make the artist\'s pigment ultramarine?": "Lapiz lazuli",
            "Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?": "chicago",
            "What city is the MIA gallery in?": "Minneapolis"  # extra question to test checking all questions correct
            }

space_dict = {"Which planet is closest to the sun?": "Mercury",
              "Which planet spins in the opposite direction to all the others in the solar system?": "Venus",
              "How many moons does Mars have?": '2'}


# store all the topic questions in one dictionary so can manage together, and also add/remove topics 
question_bank = { 'art': art_dict, 'space': space_dict}


#this is the main function that asks whether the user wants art or space question
def main():
    topic = validate_topic()
    play_quiz(topic)


#this is a function that validate the topic and display users with thier prefered question
# this also asks the questions, so can you use a more specific function name?
# separate validation and the quiz into separate functions 
def validate_topic():
    while True:
        topic = input('Would you like art or space question?').lower()
        if topic not in question_bank:  # if it is not one of the keys,
            print('This is not a valid topic!') #saying the topic is invalid
        else:
            return topic
            

def play_quiz(topic):
    total_score = 0

    print(f"you choose {topic}, here are your questions:  ")

    topic_dict = question_bank[topic]

    for question, correct_answer in topic_dict.items():  # iterate over key.. include the values
        print(question)  # printing the question
        user_answer = input('enter your answers and press enter: ')#input the answer
        points_earned_for_question = check_answer(user_answer, correct_answer)#this is to validate the answwer for the art
        total_score = total_score + points_earned_for_question  # add points earned to total score so far
    
    # use the length of the questions dictionary - the number of key-value pairs - to know how many 
    # questions there were. 
    total_questions = len(topic_dict)

    print(f'your total score is {total_score}/{total_questions}')#this will print out the result out of 3

    # todo - did user get all questions correct? 
    if total_score == total_questions:
        print(f'You got all {total_questions} correct!')

    
    # save repeating for each topic 

    # elif topic.casefold() == 'space':#if not the user should choose space
    #     print(f"you choose {topic}, here are your questions:  ")#and the same thing will happen over here
    #     for question, correct_answer in space_dict.items():
    #         print(question)
    #         user_answer = input('enter your answer and press enter: ')
    #         points_earned = space_answer(user_answer, correct_answer)
    #     print(f'Your total score is {total_score }/3')
    # else:
    #     while topic.casefold() != 'art' or 'space':#if the user choose either of the topic it will return to the main saying the
    #         return main()  # avoid calling main to re-start your project, using a loop to ask for input again is better https://github.com/claraj/while_loop_vs_recursion


# make this function more general - art_answer is almost identical to space_answer so can re-use the same function for both
def check_answer(user_answer, correct_answer):
    # check if right or wrong? Return points earned for question
    if user_answer.lower() == correct_answer.lower():  # correct!
        print('Correct!')
        return 1  # earned one point
    else:
        print(f'Sorry, that is not the right answer. The correct answer is {correct_answer}.')
        return 0 #earn 0 point if anwswer is wrong
    print('End of quiz!')
        # no points


# def space_answer(user_answer, correct_answer):
#     # check if right or wrong? Return points earned for question
#     if user_answer.lower() == correct_answer.lower():  # correct!
#         print('Correct!')
#         return 1  # earned one point
#     else:
#         print(f'Sorry, that is not the right answer. The correct answer is {correct_answer}.')
#         return 0  # no points
#     print('End of quiz!')
main()
