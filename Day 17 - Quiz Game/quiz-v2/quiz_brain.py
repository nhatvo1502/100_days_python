import random
from question_model import Question
class QuizBrain:
    def __init__(self, ql=[]):
        self.question_number = 0
        self.question_list  = ql
        self.question_list_length = len(ql)
        self.score = 0
        self.current_question = Question()

        self.true_variants = ["True", "true", "T", "t"]
        self.false_variants = ["False", "false", "F", "f"]
    
    def show_score(self):
        print(f"Your current score is {self.score}/{self.question_number}")
    
    def show_final_score(self):
        print(f"You've completed the quiz.\nYour final score is {self.score}/{self.question_number}")

    def still_has_question(self):
        if self.question_number < self.question_list_length:
            return True
        else:
            return False

    def next_question(self):
        self.current_question = random.choice(self.question_list)
        user_answer = input(f"{self.current_question.text} (True/False): ")
        inputCorrect = False
        while not inputCorrect:
            if user_answer in self.true_variants:
                user_answer = "true"
                inputCorrect = True
            elif user_answer in self.false_variants:
                user_answer = "false"
                inputCorrect = True
            else:
                user_answer = input("Wrong input. Please try again (True/False): )")

        self.question_list.remove(self.current_question)
        return user_answer

    def check_answer(self, answer, user_answer):
        
        if user_answer.lower() == answer.lower():
            self.score+=1
            isCorrect = True
            print("You got it right!")
        else:
            print("That's wrong!")
        self.question_number+=1
        print("\n")
    
    def play(self):
        stillPlaying = True
        while stillPlaying:
            user_answer = self.next_question()
            self.check_answer(self.current_question.answer, user_answer)
            stillPlaying = self.still_has_question()
            if stillPlaying == True:
                self.show_score()
            else:
                self.show_final_score()
            
