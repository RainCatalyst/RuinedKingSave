import configparser, mouse, keyboard
from re import L

# Initialize config
config = configparser.ConfigParser() 
config.read('config.ini')

if not config.has_section('user'):
    config.add_section('user')
    config['user']['save_shortcut'] = 'ctrl+s'
    config['user']['save_slot'] = '0'

if not config.has_section('buttons'):
    config.add_section('buttons')

# Wait for key press
print('Hover the load/save button in the game window and press space.')
keyboard.wait('space')

# Store mouse position
config['buttons']['saveload'] = str(mouse.get_position()) 

# Save config
with open('config.ini', 'w+') as f:
    config.write(f) 

print('Config updated.')