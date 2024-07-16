from data import questions
from question_model import Question

question_bank = []
score = 0
for question in questions:
    question_bank.append(Question(question["question"], question["answer"]))


for question in question_bank:
    user_answer = input(question.question + ' True or False? ').lower()
    if user_answer == question.answer.lower():
        print('Correct')
        score += 1
        print(f'Current Score: {score}')
    else:
        print('Incorrect')
        print(f'Current Score: {score}')

print(f'Final Score: {score}')
