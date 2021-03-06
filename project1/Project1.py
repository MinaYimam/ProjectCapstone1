""" A quiz program. """
"""THIS IS A DICTIONARY HOLDING A QUESTION AND AN ANSWER OF ART AND SPACE QUESTION
THE USER WILL BE ASKED IF THEY WANT AN ART OR A SPACE QUESTION AND BASED ON THEIR INPUT THIS FUNCITON WILL IDENTIFY IF 
THE USER ANSWERED CORRECT OR NOT AND WILL SHOW HOW MANY CORRECT ANSWER THEY GOT FROM THE WHOLE QUESTION"""
art_dict = {"Who painted the Mona Lisa?": "Leonardo da vinci",
            "What precious stone is used to make the artist\'s pigment ultramarine?": "Lapiz lazuli",
            "Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?": "chicago"}

space_dict = {"Which planet is closest to the sun?": "Mercury",
              "Which planet spins in the opposite direction to all the others in the solar system?": "Venus",
              "How many moons does Mars have?": '2'}

#this is the main function that asks whether the user wants art or space question
def main():
    topic = input('Would you like art or space question?')
    validate_topic(topic)

#this is a function that validate the topic and display users with thier prefered question
def validate_topic(topic):
    total_score = 0
    if topic.casefold() == 'art':
        print(f"you choose {topic}, here are your questions:  ")
        for question, correct_answer in art_dict.items():  # iterate over key.. include the values
            print(question)  # printing the question
            user_answer = input('enter your answers and press enter: ')#input the answer
            points_earned_for_question = art_answer(user_answer, correct_answer)#this is to validate the answwer for the art
            total_score = total_score + points_earned_for_question  # add points earned to total score so far
        print(f'your total score is {total_score}/3')#this will print out the result out of 3
    elif topic.casefold() == 'space':#if not the user should choose space
        print(f"you choose {topic}, here are your questions:  ")#and the same thing will happen over here
        for question, correct_answer in space_dict.items():
            print(question)
            user_answer = input('enter your answer and press enter: ')
            points_earned = space_answer(user_answer, correct_answer)
        print(f'Your total score is {total_score }/3')
    else:
        while topic.casefold() != 'art' or 'space':#if the user choose either of the topic it will return to the main saying the
            print('This is not a valid topic!')#saying the topic is invalid
            return main()


def art_answer(user_answer, correct_answer):
    # check if right or wrong? Return points earned for question
    if user_answer.lower() == correct_answer.lower():  # correct!
        print('Correct!')
        return 1  # earned one point
    else:
        print(f'Sorry, that is not the right answer. The correct answer is {correct_answer}.')
        return 0 #earn 0 point if anwswer is wrong
    print('End of quiz!')
        # no points


def space_answer(user_answer, correct_answer):
    # check if right or wrong? Return points earned for question
    if user_answer.lower() == correct_answer.lower():  # correct!
        print('Correct!')
        return 1  # earned one point
    else:
        print(f'Sorry, that is not the right answer. The correct answer is {correct_answer}.')
        return 0  # no points
    print('End of quiz!')
main()
