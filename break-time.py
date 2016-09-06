# simple program that opens a youtube link every X seconds to
# remind you that is time to have some break from the PC
# total_breaks, break_length and link_video can be changed

import webbrowser
import time

break_count = 0
# update your preferred values below
total_breaks = 3
break_length = 10
link_video = "https://youtu.be/PT2_F-1esPk?t=10s"

print("You have strarted the program on "+time.ctime())
while (break_count < total_breaks):
    time.sleep(break_length)
    webbrowser.open(link_video)
    break_count = break_count + 1
