""" A quiz program. """
"""creating dictionaries
funtion"""
arts = {"art": {"Who painted the Mona Lisa?": "Leonardo da vinci",
                    "What precious stone is used to make the artist\'s pigment ultramarine?": "Lapiz lazuli",
                    "Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?": "chicago"}}
spacedict = {"space": {"Which planet is closest to the sun?": "Mercury",
                     "Which planet spins in the opposite direction to all the others in the solar system?": "Venus",
                     "How many moons does Mars have?" : '2'}}
#print(dictionary)

total_score = 0

for key, value in dictionary1.items():
    print(f'topics:{value}')
def main():
    total_score = 0
    for key, value in dictionary1.items():
        print(f'topics:{value}')
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
    """for i in dictionary:
        print(i)
        print(input('enter your answers?'))"""
    """if validate_q == dictionary["art"]:
        for key, value in dictionary.keys():
            print(value)"""



"""def check_answers(answer):
    if answer == dictionary1():
        return "good job"
    else:
        f'you answered wrong the, the answer is {dictionary1()} '"""


def validate_q(question):
    while question not in dictionary1.keys():
        for key, value in dictionary1.items():
            print(key)
        question = input('You can only choose one of the topics?')

        #question = input('Would you like art or space question?')
    else:
        return question


main()
