import webbrowser
import time

total_breaks = 3
break_count = 0
break_length = 10

print("You have strarted the program on "+time.ctime())



while (break_count < total_breaks):
    time.sleep(break_length)
    webbrowser.open("https://youtu.be/PT2_F-1esPk?t=10s")
    break_count = break_count + 1
