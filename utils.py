import mouse, keyboard
from time import sleep

def move_and_click(position: tuple, delay: float = 0):
    mouse.move(*position)
    sleep(delay)
    mouse.click()

def press_and_wait(keys: str, delay: float):
    keyboard.press_and_release(keys)
    sleep(delay)