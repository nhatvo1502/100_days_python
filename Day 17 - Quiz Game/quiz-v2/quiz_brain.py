import random
class QuizBrain:
    def __init__(self, ql):
        self.question_number = 0
        self.question_list  = ql
    
    def next_question(self):
        user_answer = input(f"")