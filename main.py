from playsound import playsound
import tkinter as tk
import time

window = tk.Tk()
timing_text = tk.Label(text="00:00.00", width=10, height=10)
timeAmt = 21.0
is_paused = False


def display_time(val):
    minutes = int(val // 60)
    seconds = val % 60
    return f"{minutes:02d}:{seconds:0>5.2f}"


def timer_start():
    global is_paused
    is_paused = False

    def timer_loop():
        if not is_paused:
            global timeAmt
            timeAmt = max(round(timeAmt - 0.010, 2), 0)
            timing_text["text"] = display_time(timeAmt)

            if timeAmt == 20.0:
                playsound("Alarm.mp3", False)

            if timeAmt == 0.0:
                playsound("beep.mp3", False)
                return

            window.after(10, timer_loop)

    timer_loop()


def timer_pause():
    global is_paused
    is_paused = True


btn_start = tk.Button(
    master=window,
    text="START",
    command=timer_start
)

btn_pause = tk.Button(
    master=window,
    text="PAUSE",
    command=timer_pause
)

btn_start.grid(row=0, column=0, padx=10)
timing_text.grid(row=0, column=1, padx=10)
btn_pause.grid(row=0, column=2, padx=10)

window.mainloop()
