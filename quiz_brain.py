from data import questions


class QuizBrain:
    def __init__(self, questions_bank):
        self.questions = questions_bank
        self.score = 0
        self.question_number = 1

    def start_quiz(self):
        self.ask_question()

    def ask_question(self):
        for question in self.questions:
            answer = input(f"Q{self.question_number}. {question.question} True or False? ").lower()
            self.check_answer(answer)

    def check_answer(self, answer):
        if answer.lower() == self.questions[self.question_number - 1].answer.lower():
            print('Correct')
            self.score += 1
            self.question_number += 1
            if self.print_final_score():
                return
            else:
                print(f'Current Score: {self.score}')
        else:
            print('Incorrect')
            print(f"The correct answer was {self.questions[self.question_number - 1].answer}")
            self.question_number += 1
            if self.print_final_score():
                return
            else:
                print(f'Current Score: {self.score}')

    def print_final_score(self):
        if self.question_number > len(questions):
            print(f'Final Score: {self.score}')
            return True
        else:
            return False

