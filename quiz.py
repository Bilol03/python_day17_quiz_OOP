from data import question_data
import random
class Quiz:
    def __init__(self, question_data):
        self.question_data = question_data

    def give_question(self):
        self.question = random.choice(self.question_data)
        return self.question['text']

    def answer(self):
        return self.question['answer']
    def check_answer(self, answer):
       if self.question['answer'].lower() == answer.lower():
           return True
       else:
           return False


quiz = Quiz(question_data)

question_num = 1
score = 0
end_quiz = False
while not end_quiz:
    user_answer = input(f"Q.{question_num}: {quiz.give_question()} True/Flase? : ")
    if quiz.check_answer(user_answer):
        print("You got right")
        print(f"Correct asnwer was {quiz.answer()}")
        score += 1
        print(f"Your current score is: {score}/{question_num}")
    else:
        print("That's wrong")
        print(f"Correct asnwer was {quiz.answer()}")
        print(f"Your current score is: {score}/{question_num}")
        end_quiz = True

    question_num += 1




