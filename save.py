import configparser, keyboard
from time import sleep
from utils import move_and_click, press_and_wait

# Load config
config = configparser.ConfigParser()

try:
    with open('config.ini') as f:
        config.read_file(f)
except IOError as e:
    raise Exception('Unable to load config, make sure to generate it first using configure.py.') from e

saveload_position = tuple(map(int, config['buttons']['saveload'][1:-1].split(',')))
slot_index = int(config['user']['save_slot'])

# Save shortcut
def save():
    press_and_wait('tab', 0.3)
    move_and_click(saveload_position, 0.05)
    sleep(0.55)
    press_and_wait('e', 0.45)
    for _ in range(slot_index):
        press_and_wait('s', 0.25)
    press_and_wait('e', 0.05)
    press_and_wait('a', 0.5)
    press_and_wait('e', 0.2)
    press_and_wait('esc', 0.5)
    press_and_wait('esc', 0.5)
    press_and_wait('esc', 0.05)
    print('Saved game.')

# Attach save callback
keyboard.add_hotkey(config['user']['save_shortcut'], save)

# Wait for exit
print('Press Ctrl + C to exit')
keyboard.wait()