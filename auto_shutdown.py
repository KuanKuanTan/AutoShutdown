import time
import os
from tkinter import *
import tkinter as tk
shutdown_sec = 0
shutdown_hour = 0
shutdown_min = 0
hour_now = 0
min_now = 0
entrymin = 0
windows = Tk()
windows.title("Auto Shutdown")
canvas = Canvas(windows, width=500, height=160, bg = 'white')
canvas.pack()
def shutdowntime():
    entrymin = int(entry2.get())
    hour_now = int(time.strftime("%H"))
    min_now = int(time.strftime("%M"))
    if int(entry2.get()) < min_now:
        shutdown_hour = int(entry1.get()) -1 - hour_now
        shutdown_min = int(entry2.get()) + 60 - min_now
    else:
        shutdown_hour = int(entry1.get()) - hour_now
        shutdown_min = int(entry2.get()) - min_now
    shutdown_sec = int(shutdown_hour) * 60 * 60 + int(shutdown_min) * 60
    windows.destroy()
    time.sleep(shutdown_sec)
    print("shutdown")
    os.system('shutdown -s')
label1 = tk.Label(windows, text = "Hour")
label1.pack()
entry1 = tk.Entry(windows, text = "")
entry1.pack()
label2 = tk.Label(windows, text = "Min")
label2.pack()
entry2 = tk.Entry(windows, text = "")
entry2.pack()
canvas.create_text(250, 50, text= 'Auto Shutdown', fill='black', font = ('Helvetica', 30))
canvas.create_text(250, 130, text= "您按下前往後視窗會關閉，但程序會繼續", fill="red", font = ("Helvetica", 10))
canvas.create_text(250, 150, text= "請您以24小時制方式輸入，電腦會在您輸入時間關機", fill="red", font = ("Helvetica", 10))
button1 = Button(windows, text="Go!", command =shutdowntime)
button1.pack()
windows.mainloop()
#by YKI