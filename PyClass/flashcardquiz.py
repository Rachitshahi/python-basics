import random

# flash card quiz game
qna = [("Which country has the highest life expectancy?", "Hong Kong"),
       ("What is the most common surname in the United States?", "Smith"),
       ("Who was the Ancient Greek God of the Sun?", "Apollo"),
       ("How many minutes are in a full week?", "10,080"),
       ("Aureolin is a shade of what color?", "Yellow")]

def play_qna(qna):
    question, answer = random.choice(qna)
    user_input = input(question + " ")
    if user_input.strip().lower() == answer.lower():
        print("Correct!")
    else:
        print(f"Wrong! The correct answer was: {answer}")

play_qna(qna)
