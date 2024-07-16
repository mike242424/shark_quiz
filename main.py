from data import questions
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
quiz_brain = QuizBrain(question_bank)
for question in questions["results"]:
    question_bank.append(Question(question["question"], question["correct_answer"]))


quiz_brain.start_quiz()
