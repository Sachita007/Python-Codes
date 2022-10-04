from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
marks =""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer,marks, reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_lebel.config(text="Timer")
    label_check.config(text="")
    marks = ""


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count():
    global reps
    reps += 1
    if reps % 8 == 0:

        timer_lebel.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:

        timer_lebel.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:

        timer_lebel.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        start_count()

        global reps, marks
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✔"
        label_check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_lebel = Label(text="Timer")
timer_lebel.config(font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
timer_lebel.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

button_start = Button(text="Start", command=start_count)
button_start.config(fg="black", pady=1, padx=7, highlightthickness=0)
button_start.grid(row=2, column=0)

button_stop = Button(text="Reset", command=reset_timer)
button_stop.config(fg="black", pady=1, padx=5, highlightthickness=0)
button_stop.grid(row=2, column=2)

label_check = Label()
label_check.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
label_check.grid(row=3, column=1)

window.mainloop()
