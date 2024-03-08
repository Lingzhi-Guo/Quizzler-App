from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score:0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some text.",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.check_answer_true)
        self.true_button.grid(row=2, column=1)
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.check_answer_false)
        self.false_button.grid(row=2, column=0)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text, fill=THEME_COLOR)
            self.canvas.config(bg="white")
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've completed the quiz!\nYour final score was: "
                     f"{self.quiz.score}/{self.quiz.question_number}",
                font=("Arial", 25, "bold"),
                fill=THEME_COLOR)
            self.canvas.config(bg="white")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_answer_true(self):
        if self.quiz.check_answer("true"):
            self.give_feedback("true")
        else:
            self.give_feedback("false")
        self.window.after(1000, func=self.get_next_question)

    def check_answer_false(self):
        if self.quiz.check_answer("true"):
            self.give_feedback("true")
        else:
            self.give_feedback("false")
        self.window.after(1000, func=self.get_next_question)

    def give_feedback(self, true_or_false):
        self.score_label.config(text=f"Score:{self.quiz.score}")
        if true_or_false == "true":
            self.canvas.itemconfig(self.question_text,
                                   text="You got the answer right!",
                                   font=("Arial", 20, "normal"),
                                   fill="white")
            self.canvas.config(bg="green")
        else:
            self.canvas.itemconfig(self.question_text,
                                   text="You got the answer wrong!",
                                   font=("Arial", 20, "normal"))
            self.canvas.config(bg="red")
