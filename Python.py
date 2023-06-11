
import random

def run_personality_test():

    questions = [

        "Was science your favorite area?",

        "Did you hate any of the science subjects?",

        "How often did you attend science classes?",

        "How did you like your teacher?",

        "Are you naturally curious about the world around you?",

        "Do you enjoy solving puzzles or brain teasers?",

        "How comfortable are you with abstract or theoretical concepts?",

        "Are you detail-oriented and meticulous in your work?",

        "How comfortable are you with public speaking or presenting information to others?",

        "Are you a natural leader and enjoy taking charge of projects or teams?",

        "How well do you adapt to new situations or changes?",

        "Do you enjoy working independently or as part of a team?",

        "Are you patient and persistent when faced with challenges?",

        "How well do you handle stress and pressure?",

        "How much do you enjoy expressing yourself through creative outlets?",

        "Are you naturally drawn to visual aesthetics and design?",

        "How comfortable are you with experimenting and trying out new artistic techniques?",

        "Do you enjoy visiting art galleries and exhibitions?",

        "How often do you engage in artistic activities during your free time?",

        "Are you passionate about storytelling and conveying emotions through art?",

        "How comfortable are you with thinking outside the box and embracing unconventional ideas?",

        "Do you enjoy working with different mediums such as paints, clay, or digital tools?",

        "How well do you handle constructive criticism and feedback on your artistic work?",

        "Are you motivated by the process of creating art rather than the end result?",

        "Do you enjoy contemplating deep philosophical questions?",

        "Are you interested in exploring the nature of knowledge and reality?",

        "How comfortable are you with abstract and complex philosophical concepts?",

        "Do you enjoy engaging in debates and discussions about moral and ethical dilemmas?",

        "Are you fascinated by the study of human existence and the meaning of life?",

        "How well do you critically analyze and evaluate arguments and ideas?",

        "Do you enjoy reading philosophical texts and exploring different philosophical traditions?"

    ]

    random.shuffle(questions)  # Shuffle the questions randomly

    selected_questions = random.sample(questions, 10)  # Select 10 random questions

    total_score = 0

    print("Please answer each question with 'yes' or 'no'.")

    print("If your answer is 'no', the score for that question will be 0.")

    for question in selected_questions:

        while True:

            answer = input(question + " (yes/no): ").lower()

            if answer == "yes":

                while True:

                    score = input("Enter a value from 1-10 where 10 is the highest: ")

                    if score.isdigit():

                        score = int(score)

                        if 1 <= score <= 10:

                            total_score += score

                            break

                        else:

                            print("Invalid input! Please enter a number between 1 and 10.")

                    else:

                        print("Invalid input! Please enter a number between 1 and 10.")

                break

            elif answer == "no":

                total_score += 0

                break

            else:

                print("Invalid input! Please enter either 'yes' or 'no'.")

    if total_score < 50:

        print("Based on your score, you may have an inclination towards an art career.")

    elif 50 <= total_score < 70:

        print("Based on your score, you may have an inclination towards a philosophical career .")

    elif total_score >= 70:

        print("Based on your score, you may have an inclination towards a science course.")

run_personality_test()
