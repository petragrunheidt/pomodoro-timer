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
CHECK_MARK = "✔"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    global reps
    window.after_cancel(timer)
    title_label["text"] = "Timer"
    title_label["fg"] = GREEN
    check_label["text"] = ""
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_start():
    global reps

    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label["text"] = "Break!"
        title_label["fg"] = PINK
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label["text"] = "Break!"
        title_label["fg"] = RED
    elif reps % 2 != 0:
        count_down(WORK_MIN * 60)
        title_label["text"] = "Work!"
        title_label["fg"] = GREEN


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    timer = window.after(1000, count_down, count - 1)
    if count_min == 0 and count_sec == "00":
        if reps % 2 != 0:
            check_label["text"] += CHECK_MARK
        timer_start()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=220, height=250, bg=YELLOW, highlightthickness=0)
TOMATO = PhotoImage(file="tomato.png")
canvas.create_image(110, 125, image=TOMATO)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(110, 150, text="00:00", fill="white", font=("Arial", 30, "bold"))

# ---------------------------- LABELS ------------------------------- #

title_label = Label(text="Timer", fg=GREEN)
title_label.config(padx=10, pady=10, font=("Arial", 46, "italic"), bg=YELLOW)
title_label.grid(column=1, row=0)

start_button = Button(text="Start", command=timer_start, bg=RED)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=timer_reset, bg=RED)
reset_button.grid(column=2, row=2)

check_label = Label(text="", padx=10, pady=10, font=("Arial", 16, "italic"), bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

window.mainloop()
