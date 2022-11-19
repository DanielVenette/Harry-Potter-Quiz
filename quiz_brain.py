import random

# this class will be capable of checking that the quiz has questions remaining,
# scrolling to the next question, and checking to see if the user chose correctly.
# In the console version, it will also accept user answers and display the score
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.quiz_length = 10
        self.question_list = random.sample(q_list, 11)
        self.current_question = None
        # create lists of male and female actors
        self.male_actors = [x.actor for x in self.question_list if x.gender == "male"]
        self.female_actors = [x.actor for x in self.question_list if x.gender == "female"]
        # create empty list that will contain the four actor choices for user
        self.possible_actors = []

    def still_has_questions(self):
        return self.question_number <= self.quiz_length

    def next_question(self):
        # get the current number question from the question list
        self.current_question = self.question_list[self.question_number]
        # increment the question number in preparation for the following question
        self.question_number += 1
        # create a list of four possible actors to pick from (1 being the correct choice,
        # and the other 3 being randomly chosen from the list of same-gender names
        if self.current_question.gender == "male":
            incorrect_actors = random.sample(self.male_actors, 3)
            while self.current_question.actor in incorrect_actors:
                incorrect_actors = random.sample(self.male_actors, 3)
            self.possible_actors = [self.current_question.actor] + incorrect_actors
        else:
            incorrect_actors = random.sample(self.female_actors, 3)
            while self.current_question.actor in incorrect_actors:
                incorrect_actors = random.sample(self.female_actors, 3)
            self.possible_actors = [self.current_question.actor] + incorrect_actors
        random.shuffle(self.possible_actors)


    def check_answer(self, passed_user_answer) -> bool:
        correct_answer = self.current_question.actor
        if passed_user_answer == correct_answer:
            print(f"You got it!  The correct answer was {correct_answer}\n")
            self.score += 1
            return True
        else:
            print(f"Sorry, the correct answer was {correct_answer}\n")
            return False
