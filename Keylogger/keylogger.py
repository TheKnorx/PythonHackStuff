import keyboard
# from threading import Thread

rk = keyboard.record(until="Esc")

open("log.txt", "w").write(rk)

# keyboard.play(rk)
