from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(ques=question_text, answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print("You have the compeleted the Quiz")
print(f"our final score is {quiz.score}/{quiz.question_number}")
