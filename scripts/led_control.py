import time
import os

def set_led_status(status):
    mode = 'default-on' if status else 'none'
    with open('/sys/class/leds/orangepi:red:power/trigger', 'w') as f:
        f.write(mode)


modes = {
    'on': [(True, 0.5)],
    'off': [(False, 0.5)],
    'waiting_hdd': [(True, 0.1), (False, 0.1), (True, 0.1), (False, 0.8)],
    'waiting_card': [(True, 0.1), (False, 0.1), (True, 0.1), (False, 0.1), (True, 0.1), (False, 0.8)],
    'syncing': [(True, 0.2), (False, 0.2)],
}

current_mode = 'off'
control_file = '/tmp/led_mode'

while True:
    if os.path.isfile(control_file):
        with open(control_file, 'r') as f:
            current_mode = f.readline().strip()
        if not current_mode in modes:
            current_mode = 'off'
        os.remove(control_file)
        print(current_mode)
    for status, seconds in modes[current_mode]:
        set_led_status(status)
        time.sleep(seconds)


