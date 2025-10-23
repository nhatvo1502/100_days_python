from question_model import Question
from data import question_data, url
from quiz_brain import QuizBrain
import random
import requests

question_bank = []
# for question in question_data:
#     question_bank.append(Question(question['text'], question['answer']))

r = requests.get(url)
r = r.json()
for i in r["results"]:
    question_bank.append(Question(i["question"].replace("&quot;", '"').replace("&#039;", "'").replace('&rsquo;', "'"), i["correct_answer"]))

quiz = QuizBrain(question_bank)
quiz.play()