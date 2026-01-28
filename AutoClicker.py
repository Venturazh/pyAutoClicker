from pynput import mouse, keyboard
import threading
import time

mouseController = mouse.Controller()
Clicking = False


def AutoClick():
    global Clicking
    while True:
        if Clicking:
            mouseController.click(mouse.Button.left)
        time.sleep(0.01)


def DetectPress(key):
    global Clicking
    try:
        if key.char == 'z':
            Clicking = not Clicking
            print(f"State: {Clicking}")
    except AttributeError:
        if key == keyboard.Key.esc:
            return False


threading.Thread(target=AutoClick, daemon=True).start()

with keyboard.Listener(on_press=DetectPress) as listener:
    listener.join()
