from tkinter import *
from quiz_brain import QuizBrain

GRYFFINDOR_DARK_RED = "#740001"
GRYFFINDOR_LIGHT_RED = "#ae0001"
GRYFFINDOR_LIGHT_YELLOW = "#eeba30"
GRYFFINDOR_DARK_YELLOW = "#d3a625"
GRYFFINDOR_BLACK = "#000000"

class QuizInterface:

    # this line says that we must pass in an object of type QuizBrain
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz_instance = quiz_brain
        self.window = Tk()
        self.window.title("Harry Potter Actor Quiz: For Kelsey")
        self.window.config(padx=20, pady=20, bg=GRYFFINDOR_DARK_RED)
        self.window.minsize(400, 400)

        # question number tracker
        # total questions to be asked
        self.total_questions = len(self.quiz_instance.question_list)
        print(self.total_questions)
        self.question_number_tracker = Label()
        self.question_number_tracker.config(
            text=f"Question {self.quiz_instance.question_number}/{self.quiz_instance.quiz_length}",
            fg=GRYFFINDOR_LIGHT_YELLOW,
            bg=GRYFFINDOR_DARK_RED
        )
        self.question_number_tracker.grid(column=0, row=0, columnspan=2, padx=20, pady=20)

        # score
        self.score = Label()
        self.score.config(
            text=f"Score: {self.quiz_instance.score}",
            fg=GRYFFINDOR_LIGHT_YELLOW,
            bg=GRYFFINDOR_DARK_RED
        )
        self.score.grid(column=2, row=0, columnspan=2, padx=20, pady=20)

        # "Who played..." question label
        self.who_played = Label()
        self.who_played.config(
            text="Which Actor Portrayed the above Character?",
            fg=GRYFFINDOR_LIGHT_YELLOW,
            bg=GRYFFINDOR_DARK_RED
        )
        self.who_played.grid(column=0, row=2, columnspan=4, pady=20)

        # A Button
        self.a_button = Button(text="A", bg="black", fg=GRYFFINDOR_LIGHT_YELLOW,
                               width=3, height=2, command=self.choose_a
                               )
        self.a_button.grid(column=0, row=3, padx=10, pady=10)

        # B Button
        self.b_button = Button(text="B", bg="black", fg=GRYFFINDOR_LIGHT_YELLOW,
                               width=3, height=2, command=self.choose_b)
        self.b_button.grid(column=2, row=3, padx=10, pady=10)

        # C Button
        self.c_button = Button(text="C", bg="black", fg=GRYFFINDOR_LIGHT_YELLOW,
                               width=3, height=2, command=self.choose_c)
        self.c_button.grid(column=0, row=4, padx=10, pady=10)

        # D Button
        self.d_button = Button(text="D", bg="black", fg=GRYFFINDOR_LIGHT_YELLOW,
                               width=3, height=2, command=self.choose_d)
        self.d_button.grid(column=2, row=4, padx=10, pady=10)

        # run "next_question() so that there are possible actor choices available
        self.get_next_question()

        # "A" Actor
        self.a_actor = Label(
            text=self.quiz_instance.possible_actors[0],
            fg=GRYFFINDOR_LIGHT_YELLOW,
            bg=GRYFFINDOR_DARK_RED,
            anchor="w"
        )
        self.a_actor.grid(column=1, row=3, padx=10, pady=10)

        # "B" Actor
        self.b_actor = Label(
            text=self.quiz_instance.possible_actors[1],
            fg=GRYFFINDOR_LIGHT_YELLOW,
            bg=GRYFFINDOR_DARK_RED
        )
        self.b_actor.grid(column=3, row=3, padx=10, pady=10)

        # "C" Actor
        self.c_actor = Label(
            text=self.quiz_instance.possible_actors[2],
            fg=GRYFFINDOR_LIGHT_YELLOW,
            bg=GRYFFINDOR_DARK_RED
        )
        self.c_actor.grid(column=1, row=4, padx=10, pady=10)

        # "D" Actor
        self.d_actor = Label(
            text=self.quiz_instance.possible_actors[3],
            fg=GRYFFINDOR_LIGHT_YELLOW,
            bg=GRYFFINDOR_DARK_RED
        )
        self.d_actor.grid(column=3, row=4, padx=10, pady=10)

        # canvas for character name/picture (if available)
        self.canvas = Canvas()
        self.canvas.config(width=350, height=200, bg=GRYFFINDOR_DARK_YELLOW, highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=4, pady=20)
        self.character_text = self.canvas.create_text(175, 100, text=self.quiz_instance.current_question.film_character)





        self.window.mainloop()

    def choose_a(self):
        if self.quiz_instance.check_answer(self.quiz_instance.possible_actors[0]):
            self.canvas.itemconfig(self.character_text,
                                   text=f"You got it!  "
                                        f"The correct answer was {self.quiz_instance.current_question.actor}"
                                   )
        else:
            self.canvas.itemconfig(self.character_text,
                                   text=f"Sorry, the correct answer was {self.quiz_instance.current_question.actor}")
        self.canvas.after(2000, func=self.get_next_question)

    def choose_b(self):
        if self.quiz_instance.check_answer(self.quiz_instance.possible_actors[1]):
            self.canvas.itemconfig(self.character_text,
                                   text=f"You got it!  "
                                        f"The correct answer was {self.quiz_instance.current_question.actor}"
                                   )
        else:
            self.canvas.itemconfig(self.character_text,
                                   text=f"Sorry, the correct answer was {self.quiz_instance.current_question.actor}")
        self.canvas.after(2000, func=self.get_next_question)

    def choose_c(self):
        if self.quiz_instance.check_answer(self.quiz_instance.possible_actors[2]):
            self.canvas.itemconfig(self.character_text,
                                   text=f"You got it!  "
                                        f"The correct answer was {self.quiz_instance.current_question.actor}"
                                   )
        else:
            self.canvas.itemconfig(self.character_text,
                                   text=f"Sorry, the correct answer was {self.quiz_instance.current_question.actor}")
        self.canvas.after(2000, func=self.get_next_question)

    def choose_d(self):
        if self.quiz_instance.check_answer(self.quiz_instance.possible_actors[3]):
            self.canvas.itemconfig(self.character_text,
                                   text=f"You got it!  "
                                        f"The correct answer was {self.quiz_instance.current_question.actor}"
                                   )
        else:
            self.canvas.itemconfig(self.character_text,
                                   text=f"Sorry, the correct answer was {self.quiz_instance.current_question.actor}")
        self.canvas.after(2000, func=self.get_next_question)

    def get_next_question(self):
        self.quiz_instance.next_question()
        self.score.config(
            text=f"Score: {self.quiz_instance.score}"
        )
        if self.quiz_instance.still_has_questions():
            self.question_number_tracker.config(
                text=f"Question {self.quiz_instance.question_number}/{self.quiz_instance.quiz_length}"
            )
            if self.quiz_instance.question_number > 1:
                self.a_actor.config(text=self.quiz_instance.possible_actors[0])
                self.b_actor.config(text=self.quiz_instance.possible_actors[1])
                self.c_actor.config(text=self.quiz_instance.possible_actors[2])
                self.d_actor.config(text=self.quiz_instance.possible_actors[3])
                self.canvas.itemconfig(self.character_text, text=self.quiz_instance.current_question.film_character)
        else:
            self.canvas.itemconfig(self.character_text, text="You've completed the quiz.  Good Job!")
            self.a_button.config(state="disable")
            self.b_button.config(state="disable")
            self.c_button.config(state="disable")
            self.d_button.config(state="disable")