from tkinter import *
import math
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


def reset_timer():
    global reps

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks_label.config(text="")
    reps = 0


def start_timer():
    global reps
    reps += 1

    # Convert minutes to seconds
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    # Check how much time to count down
    if reps % 8 == 0:
        count_down(long_break_seconds)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_seconds)
        title_label.config(text="Work", fg=GREEN)


def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60

    # Change seconds format
    # Ex: 8 becomes 08
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    # Change the timer canvas text
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")

    # Check if the timer value greater than 0.
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # Start the next timer
        start_timer()

        # Add check mark every work timer completed
        marks = ""
        work_session = math.floor(reps / 2)

        for _ in range(work_session):
            marks += CHECK_MARK

        check_marks_label.config(text=marks)


# window SETUP
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Create Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # highlightthickness removes the canvas border
tomato_img = PhotoImage(file="tomato.png")

# Add tomato image and text
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Add Title Label
title_label = Label()
title_label.config(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

# Add start and reset button
start_button = Button(text="Start", bg="white", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg="white", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Add check marks Label
check_marks_label = Label(font=(FONT_NAME, 25), bg=YELLOW, fg=GREEN)
check_marks_label.grid(column=1, row=3)





window.mainloop()