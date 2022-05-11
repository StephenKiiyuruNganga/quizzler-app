import tkinter
from turtle import bgcolor

from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # window config
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # score label
        self.score_label = tkinter.Label()
        self.score_label.config(text="Score: 0",
                                bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        # question canvas
        self.question_canvas = tkinter.Canvas(
            width=300, height=250, bg="white")
        self.question_text = self.question_canvas.create_text(150,
                                                              125,
                                                              width=280,
                                                              text="Question text goes here",
                                                              font=("Arial",
                                                                    17,
                                                                    "italic"),
                                                              fill=THEME_COLOR)
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # buttons
        check_mark_img = tkinter.PhotoImage(file="./images/true.png")
        x_mark_img = tkinter.PhotoImage(file="./images/false.png")
        self.true_btn = tkinter.Button(
            image=check_mark_img, highlightthickness=0,  command=self.answer_true)
        self.true_btn.grid(row=2, column=0)
        self.false_btn = tkinter.Button(
            image=x_mark_img, highlightthickness=0, command=self.answer_false)
        self.false_btn.grid(row=2, column=1)

        # display question
        self.get_next_question()

        # keep the window running
        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.question_canvas.itemconfig(
                self.question_text, text=question_text, fill=THEME_COLOR)
        else:
            self.question_canvas.itemconfig(
                self.question_text, fill=THEME_COLOR, text="You have completed the quiz")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def answer_true(self):
        answer = "true"
        is_right = self.quiz.check_answer(answer)
        self.give_feedback(is_right)

    def answer_false(self):
        answer = "false"
        is_right = self.quiz.check_answer(answer)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.question_canvas.config(bg="green")
            self.question_canvas.itemconfig(self.question_text, fill="white")
        else:
            self.question_canvas.config(bg="red")
            self.question_canvas.itemconfig(self.question_text, fill="white")

        self.window.after(1000, self.get_next_question)
