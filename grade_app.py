import tkinter as tk
import math

Grades : list = []

FG_COLOR = "#FFF"
BG_COLOR = "#506DDE"
FONT = ("Helvetica", 12)
FONT_XL = ("Helvetica", 15)


class StudentGrade:
    def __init__(self, label, grade) -> None:
        self.label = label
        self.grade = grade



def calcule_avrage(notes : list) -> float:
        if(len(notes) <= 0):
            return 0.0
        _s = 0
        for n in notes:
            _s += n.grade
        return math.floor(_s / len(notes))

def show_grade(score_avrage : float) -> str:
    if(score_avrage > 100):
        return "INVALID"
    if(score_avrage < 40):
        return "F"
    if(score_avrage == 40):
        return "E"
    if(score_avrage>= 41 and score_avrage < 45):
        return "D"
    if(score_avrage >= 45 and score_avrage <= 59):
        return "C"
    if(score_avrage >= 60 and score_avrage <= 69):
        return "B"
    else:
        return "A"
    

class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.config(background=BG_COLOR)
        self.grade_label = tk.StringVar()
        self.grade = tk.IntVar()
        self.layout()
        self.row_count = 1



    @staticmethod
    def add_row(frame, n : int, gradeInstance) -> None:
        l_input = tk.Label(frame,  text=gradeInstance.label,bg=BG_COLOR, fg=FG_COLOR, font=FONT)
        lg_input = tk.Label(frame,  text=gradeInstance.grade,bg=BG_COLOR, fg=FG_COLOR, font=FONT)
        l_input.grid(row=n,column=0)
        lg_input.grid(row=n,column=1)

    def add_button_clicked(self,frame):
        if(self.grade.get() > 100):
            return
        if(self.grade.get() <= 0 or len(self.grade_label.get()) == 0):
            return
        self.row_count += 1
        gradeInstance = StudentGrade(self.grade_label.get(), self.grade.get())
        Grades.append(gradeInstance)
        App.add_row(frame,self.row_count, gradeInstance)
        self.grade_changed()
        self.grade_label.set("")
        self.grade.set(0)

    
    def grade_changed(self):
        mean = calcule_avrage(Grades)
        self.l_l.config(text=f"Current Scores Average : {mean}")
        self.grade_l.config(text=f"Grade : {show_grade(mean)}")

    def layout(self):
        self.l_l = tk.Label(self, text="...",bg=BG_COLOR, fg=FG_COLOR, font=FONT)
        self.l_l.pack(side=tk.TOP, anchor=tk.W)
        self.grade_l = tk.Label(self, text="...",bg=BG_COLOR, fg=FG_COLOR, font=FONT_XL)
        self.grade_l.pack(side=tk.TOP, anchor=tk.W)
        frame = tk.Frame(self,background=BG_COLOR)

        l_label = tk.Label(frame, text="Label", bg=BG_COLOR, fg=FG_COLOR, font=FONT)
        l_input = tk.Entry(frame,  textvariable=self.grade_label,bg=BG_COLOR, fg=FG_COLOR, font=FONT)

        g_label = tk.Label(frame, text="Grade",bg=BG_COLOR, fg=FG_COLOR, font=FONT)
        g_input = tk.Entry(frame, textvariable=self.grade,bg=BG_COLOR, fg=FG_COLOR, font=FONT)

        add_button  = tk.Button(frame, text="Add ", command=lambda : self.add_button_clicked(frame), border=1, bg=BG_COLOR, fg=FG_COLOR, font=FONT)

        l_label.grid(row=0,column=0)
        l_input.grid(row=1,column=0,ipady=5, ipadx=2)

        g_label.grid(row=0,column=1)
        g_input.grid(row=1,column=1, padx=5, ipady=5, ipadx=2)

        add_button.grid(row=1, column=2,ipady=2, ipadx=40)

        frame.pack(expand=0, side=tk.TOP)


if __name__ == "__main__":
    app = App()
    app.title("APPLICATION")
    app.geometry("550x300")
    app.resizable(False, True)
        
    app.mainloop()