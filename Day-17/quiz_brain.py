
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """returns True if questions are still to answer,
        False if there are no questions left"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """To ask next question to the user"""
        ques = self.question_list[self.question_number]
        self.question_number += 1
        # increasing ques no for moving to nxt question
        user_ans = input(
            f"Q.{self.question_number}:{ques.text} (True/False): ")
        self.check_answer(user_ans, ques.answer)

    def check_answer(self, user_ans, correct_ans):
        """To check whether the user's answer is correct or not"""
        if user_ans.lower() == correct_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's Wrong!")
        print(f"The correct answer is: {correct_ans}")
        print(f"our current score is: {self.score}/{self.question_number}")
        print("\n")
