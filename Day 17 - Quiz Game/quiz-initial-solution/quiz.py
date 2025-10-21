import random
quiz_questions = {
    "A slug's blood is green.": True,
    "The total surface area of human lungs is the size of a football pitch.": False,
    "Bananas grow on trees.": False,
    "Lightning never strikes the same place twice.": False,
    "The Great Wall of China is visible from space.": False,
    "Goldfish have a memory span of three seconds.": False,
    "Adult humans have fewer bones than babies.": True,
    "Octopuses have three hearts.": True,
    "The capital of Australia is Sydney.": False,
    "There are 1000 years in a millennium.": True,
    "Sharks are mammals.": False,
    "Venus is the hottest planet in our solar system.": True,
    "Mount Everest is the tallest mountain on Earth.": True,
    "Bats are blind.": False,
    "The human body has four lungs.": False,
    "Water boils at 100 degrees Celsius at sea level.": True,
    "Penguins can fly.": False,
    "The unicorn is the national animal of Scotland.": True,
    "Tomatoes are vegetables.": False,
    "Cows sleep standing up.": True,
    "Sound travels faster in air than in water.": False,
    "The Pacific Ocean is the largest ocean on Earth.": True,
    "Lightning is hotter than the surface of the sun.": True,
    "An ostrich’s eye is bigger than its brain.": True,
    "There are five senses in the human body.": True,
    "The Nile is the longest river in the world.": True,
    "Humans and dinosaurs lived at the same time.": False,
    "The human skeleton is made up of more than 300 bones.": False,
    "The fastest land animal is the cheetah.": True,
    "Earth is closer to the sun than Venus.": False,
    "The Great Barrier Reef is located in Australia.": True,
    "The human heart has four chambers.": True,
    "A group of crows is called a murder.": True,
    "Dogs can only see in black and white.": False,
    "Honey never spoils.": True,
    "The moon is a planet.": False,
    "The Eiffel Tower can be taller in summer.": True,
    "All mammals give birth to live young.": False,
    "Peanuts are a type of nut.": False,
    "The speed of light is faster than the speed of sound.": True,
    "Humans have walked on Mars.": False,
    "The Amazon is the largest rainforest in the world.": True,
    "Polar bears have white skin.": False,
    "An octopus has eight legs.": True,
    "The Statue of Liberty was a gift from France.": True,
    "A day on Mars is longer than a day on Earth.": True,
    "Dolphins sleep with one eye open.": True,
    "Elephants are the only animals that can’t jump.": True,
    "Spiders are insects.": False,
    "Humans share 50% of their DNA with bananas.": True
}
class Question:
    def __init__ (self, q='', a=''):
        self.question = q
        self.answer = a

class Quiz:
    def __init__(self):
        self.questions = []
        for i in quiz_questions:
            q = [i, quiz_questions[i]]
            self.questions.append(q)
        self.score = 0
        self.questions_asked = 0
        self.user_answer = ''
        self.question = ''

    def report(self):
        '''Print message'''
        print(f"Your current score is {self.score}/{self.questions_asked}")
    
    def update_score(self, isCorrected):
        '''Increase score if user answered correctly and vice versa'''
        self.questions_asked+=1
        if isCorrected == True:
            print("You got it right!")
            self.score+=1
        else:
            print("That's wrong")
    
    def pick_question(self):
        '''Return a random question'''
        self.question = random.choice(self.questions)
        return self.question
    
    def check_answer(self, user_answer):
        '''Return true or false + change score'''
        if user_answer.lower() == str(self.question[1]).lower():
            return True
        else:
            return False

    def play(self):
        '''Continue to play to game until break'''
        keep_playing = True
        while keep_playing:
        # Prompt random message + collect answer
            self.pick_question()

            answerCorrectly = False
            while not answerCorrectly:
                self.user_answer =  input(f"{self.question} (True/False)?: ")
                self.user_answer = self.user_answer.lower()
                if self.user_answer == 'true' or self.user_answer == 'false':
                    answerCorrectly = True
            
            keep_playing = self.check_answer(self.user_answer)
            # check_answer
            self.update_score(keep_playing)
            self.report()
