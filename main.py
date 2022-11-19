import requests
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

response = requests.get("https://hp-api.herokuapp.com/api/characters")
print(response)
response.raise_for_status()
entire_data_bank = response.json()

# the question bank I'll ultimately be pulling from in the
# game (not going to use the entire data bank pulled from the api)
question_bank = []
# cycle through each entry in the entire data bank and create a new list (question_bank) with only the actor,character,picture address
# data from the entire data bank.  Each entry in the new question_bank will be an object of type "Question" which will
# have four properties (film_character, actor, picture_address, gender)
for entry in entire_data_bank:
    a_film_character = entry["name"]
    a_actor = entry["actor"]
    a_picture_address = entry["image"]
    a_gender = entry["gender"]
    # only allow entries to be added which list the character and the actor who played them
    if a_film_character != "" and a_actor != "" and a_gender != "":
        new_question = Question(a_film_character, a_actor, a_picture_address, a_gender)
        question_bank.append(new_question)

for entry in question_bank:
    print(f"Character Played: {entry.film_character}")
    print(f"Gender: {entry.gender}")
    print(f"Actor: {entry.actor}")
    print(f"Picture Address: {entry.picture_address}\n")

print(len(question_bank))

quiz_brain_instance = QuizBrain(question_bank)
# print(qb.male_actors)
# print(len(qb.male_actors))
# print(qb.female_actors)
# print(len(qb.female_actors))
# for x in range(3):
#     quiz.next_question()
quiz_ui = QuizInterface(quiz_brain_instance)