
import pyautogui as keyboard

class InputHandler:

    # convert keypad notation to keyboard inputs
    _button_map = { 
        '1':('a', 's'),
        '2':('s',),
        '3':('s', 'd'),
        '4':('a',),
        '5':('',),
        '6':('d',),
        '7':('a', 'w'),
        '8':('w',),
        '9':('w', 'd'),
        'p':('u',),
        'k':('j',),
        's':('i',),
        'h':('k',),
        'd':('o',),
        }

    def __init__(self):
        keyboard.PAUSE = 0.02

    # performs motion input
    def do_move(self, input_sequence, is_left_side):
        down_keys = []

        for input in input_sequence:
            try:   
                key_inputs = InputHandler._button_map[input]
                for key in key_inputs:
                    keyboard.keyDown(key)
                    if key not in down_keys:
                        down_keys.append(key)
                    for down_key in down_keys:
                        if down_key not in key_inputs:
                            keyboard.keyUp(down_key)
                            down_keys.remove(down_key)

            except KeyError:
                print(f'{input_sequence} is an invalid input sequence')

        # release all keys after performing move
        for down_key in down_keys:
            keyboard.keyUp(down_key, _pause=False)