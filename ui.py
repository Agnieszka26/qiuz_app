from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
Q_FONT = ("Arial",20, "italic")
S_FONT = ("Arial", 16, "normal")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, font=S_FONT, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_canvas = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question",
            fill=THEME_COLOR,
            font=Q_FONT )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_img, width=70, height=70, highlightthickness=0, command= lambda: self.check_user_answer(True))
        self.true_button.config(pady=20)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=self.false_img, width=70, height=70, highlightthickness=0, command= lambda: self.check_user_answer(False))
        self.false_button.config(pady=20)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_canvas, text=q_text)
        else:
            self.canvas.itemconfig(self.question_canvas, text=f"You have reached the end of the quiz. \n Your final score is {self.quiz.score}/{self.quiz.question_number}.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_user_answer(self, answer:bool):
       self.give_feedback(self.quiz.check_answer(answer))

    def give_feedback(self, is_right):
        if is_right:
           self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
